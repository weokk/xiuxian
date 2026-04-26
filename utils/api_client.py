"""
职场修仙大护法 - API 客户端封装
支持 OpenAI 兼容 API（DeepSeek 等），含重试、错误处理、连通性测试。
"""

import time
import json
import httpx
from openai import OpenAI, APIError, APIConnectionError, APITimeoutError, AuthenticationError, RateLimitError

from utils.config import (
    API_DEFAULT_TIMEOUT, API_MAX_TOKENS, API_TEMPERATURE,
    API_MAX_RETRIES, API_RETRY_DELAY, API_TEST_TIMEOUT,
)


def get_client(api_url: str, api_key: str):
    """创建 OpenAI 兼容客户端"""
    return OpenAI(
        base_url=api_url,
        api_key=api_key,
        timeout=httpx.Timeout(API_DEFAULT_TIMEOUT, connect=10.0),
    )


def test_connection(api_url: str, api_key: str, model_name: str) -> tuple:
    """
    测试 API 连通性。
    主方案：GET /v1/models
    Fallback：发送极短测试消息

    :return: (success: bool, message: str)
    """
    # 方案1：尝试调用 /v1/models
    try:
        client = get_client(api_url, api_key)
        models = client.models.list()
        # 如果能列出模型，说明连通
        model_list = [m.id for m in models.data] if models.data else []
        model_found = model_name in model_list if model_list else True  # 有模型列表但找不到也算连通
        if model_found:
            return True, f"连接成功，可用模型：{', '.join(model_list[:5])}{'...' if len(model_list) > 5 else ''}"
        else:
            return True, f"连接成功，但未找到模型 '{model_name}'，可用模型：{', '.join(model_list[:5])}"
    except AuthenticationError:
        return False, "API Key 无效，请检查配置"
    except (APIConnectionError, APITimeoutError):
        pass  # 走 fallback
    except Exception:
        pass  # 走 fallback

    # 方案2：发送极短测试消息
    try:
        client = get_client(api_url, api_key)
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": "hi"}],
            max_tokens=5,
            timeout=httpx.Timeout(API_TEST_TIMEOUT, connect=5.0),
        )
        if response.choices and response.choices[0].message.content:
            return True, "连接成功"
        return True, "连接成功（但响应为空，请检查模型配置）"
    except AuthenticationError:
        return False, "API Key 无效，请检查配置"
    except RateLimitError:
        return True, "连接成功（触发限流，API 可用）"
    except APITimeoutError:
        return False, f"连接超时（{API_TEST_TIMEOUT}秒），请检查 API 地址"
    except APIConnectionError:
        return False, "无法连接到 API 服务器，请检查网络和 API 地址"
    except Exception as e:
        return False, f"连接失败：{str(e)[:100]}"


def chat_stream(system_prompt: str, user_prompt: str,
                api_url: str, api_key: str, model_name: str):
    """
    流式调用 AI API，返回生成器。
    每次yield一个文本片段。

    :param system_prompt: 系统提示词
    :param user_prompt: 用户消息
    :param api_url: API 地址
    :param api_key: API Key
    :param model_name: 模型名称
    :return: generator yielding str chunks
    """
    client = get_client(api_url, api_key)

    def _stream():
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=API_TEMPERATURE,
                max_tokens=API_MAX_TOKENS,
                stream=True,
            )
            finish_reason = None
            for chunk in response:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
                if chunk.choices and chunk.choices[0].finish_reason:
                    finish_reason = chunk.choices[0].finish_reason

            # 检查是否被截断（静默处理，不打断阅读体验）
            # if finish_reason == "length":
            #     yield "\n\n> ⚠️ 大护法灵力耗尽，建议拆分问题后重试。"

        except AuthenticationError:
            yield f"\n\n> ❌ API Key 无效，请检查配置。"
        except APITimeoutError:
            yield f"\n\n> ❌ 请求超时，请稍后重试。"
        except RateLimitError:
            yield f"\n\n> ❌ 请求过于频繁，请等待30秒后重试。"
        except APIConnectionError:
            yield f"\n\n> ❌ 无法连接到 API 服务器，请检查网络。"
        except Exception as e:
            yield f"\n\n> ❌ 请求失败：{str(e)[:100]}"

    return _stream()


def chat_with_retry(system_prompt: str, user_prompt: str,
                    api_url: str, api_key: str, model_name: str) -> str:
    """
    非流式调用（带重试），用于降级场景。
    :return: 完整的响应文本
    """
    last_error = None
    for attempt in range(API_MAX_RETRIES + 1):
        try:
            client = get_client(api_url, api_key)
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=API_TEMPERATURE,
                max_tokens=API_MAX_TOKENS,
                stream=False,
            )
            content = response.choices[0].message.content if response.choices else ""
            finish_reason = response.choices[0].finish_reason if response.choices else None
            if finish_reason == "length":
                content += "\n\n> ⚠️ 大护法灵力耗尽，建议拆分问题后重试。"
            return content
        except AuthenticationError as e:
            return f"❌ API Key 无效，请检查配置。"
        except (APITimeoutError, APIConnectionError) as e:
            last_error = e
            if attempt < API_MAX_RETRIES:
                time.sleep(API_RETRY_DELAY)
            continue
        except RateLimitError:
            return "❌ 请求过于频繁，请等待30秒后重试。"
        except Exception as e:
            last_error = e
            if attempt < API_MAX_RETRIES:
                time.sleep(API_RETRY_DELAY)
            continue
    return f"❌ 请求失败，已重试{API_MAX_RETRIES}次：{str(last_error)[:100]}"
