"""
职场修仙大护法 - 各场景输入表单与输出渲染
"""

import streamlit as st
from utils.config import SCENES, USER_INPUT_MAX_LENGTH, ANTI_SPAM_INTERVAL
from utils.theme import get_scene_name, get_scene_icon, is_xianxia, get_ai_name, get_consulting_text, get_fallback_title
from utils.prompts import build_prompt
from utils.api_client import chat_stream, chat_with_retry
from utils.history import add_history
from utils.components import render_disclaimer, render_example_questions
from utils.data.fallback import FALLBACK_CONTENT
import time


def render_scene_input(scene_id: int) -> dict:
    """渲染场景输入表单，返回用户输入字典"""
    scene = SCENES.get(scene_id, {})
    schema = scene.get("inputs_schema", [])
    user_inputs = {}

    # 场景标题
    name = get_scene_name(scene_id)
    icon = get_scene_icon(scene_id)
    desc = scene.get("description", "")
    st.markdown(f"## {icon} {name}")
    st.caption(desc)
    st.markdown("---")

    # 渲染示例问题
    render_example_questions(scene_id)

    # 渲染表单字段
    for field in schema:
        key = field["key"]
        field_type = field["type"]
        required = field.get("required", False)
        label = field["label"]
        placeholder = field.get("placeholder", "")
        options = field.get("options", [])

        # 必填标记
        display_label = f"**{label}** {'*' if required else ''}"
        if not required:
            display_label += "（选填）"

        # session_state key
        state_key = f"input_{key}"

        if field_type == "text":
            user_inputs[key] = st.text_input(
                display_label,
                placeholder=placeholder,
                key=state_key,
                max_chars=200,
            )
        elif field_type == "textarea":
            user_inputs[key] = st.text_area(
                display_label,
                placeholder=placeholder,
                key=state_key,
                height=100,
                max_chars=USER_INPUT_MAX_LENGTH,
            )
        elif field_type == "number":
            min_val = field.get("min_val", 0)
            max_val = field.get("max_val", 9999)
            user_inputs[key] = st.number_input(
                display_label,
                min_value=min_val,
                max_value=max_val,
                placeholder=placeholder,
                key=state_key,
            )
        elif field_type == "select":
            user_inputs[key] = st.selectbox(
                display_label,
                options=options,
                key=state_key,
            )

    return user_inputs


def validate_inputs(scene_id: int, user_inputs: dict) -> tuple:
    """验证表单输入，返回 (is_valid, error_messages)"""
    scene = SCENES.get(scene_id, {})
    schema = scene.get("inputs_schema", [])
    errors = []

    for field in schema:
        key = field["key"]
        required = field.get("required", False)
        label = field["label"]
        value = user_inputs.get(key)

        if required:
            if value is None or value == "" or value == 0:
                errors.append(f"请填写「{label}」")

    return len(errors) == 0, errors


def render_scene_output(scene_id: int, user_inputs: dict, api_url: str, api_key: str, model_name: str):
    """渲染场景输出（流式AI响应）"""
    scene = SCENES.get(scene_id, {})
    name = get_scene_name(scene_id)

    # 检查API配置
    if not api_url or not api_key or not model_name:
        _render_fallback(scene_id)
        return

    # 检查防刷
    last_consult = st.session_state.get("last_consult_time", 0)
    if time.time() - last_consult < ANTI_SPAM_INTERVAL:
        remaining = int(ANTI_SPAM_INTERVAL - (time.time() - last_consult))
        st.warning(f"请等待 {remaining} 秒后再咨询")
        return

    # 组装Prompt
    theme_mode = "xianxia" if is_xianxia() else "workplace"
    try:
        system_prompt, user_prompt = build_prompt(scene_id, theme_mode, user_inputs)
    except Exception as e:
        st.error(f"Prompt组装失败：{e}")
        return

    # Token预估（粗估：每100汉字≈150 tokens）
    total_chars = len(system_prompt) + len(user_prompt)
    estimated_tokens = total_chars // 100 * 150
    st.caption(f"📝 本次咨询预计消耗约 {estimated_tokens} tokens")

    # 开始咨询按钮
    ai_name = get_ai_name()
    if st.button(f"🔮 开始咨询", type="primary", use_container_width=True, key="consult_btn"):
        st.session_state["consulting"] = True
        st.session_state["last_consult_time"] = time.time()

    # 流式输出
    if st.session_state.get("consulting", False):
        st.markdown("---")
        consulting_text = get_consulting_text()
        st.info(consulting_text)

        try:
            stream = chat_stream(system_prompt, user_prompt, api_url, api_key, model_name)
            full_response = st.write_stream(stream)

            # 保存历史记录
            add_history(
                scene_id=scene_id,
                scene_name=name,
                user_input=user_inputs,
                ai_output=full_response,
                theme_mode=theme_mode,
            )

            # 渲染免责声明
            render_disclaimer(scene_id)

        except Exception as e:
            st.error(f"咨询失败：{e}")
            _render_fallback(scene_id)
        finally:
            st.session_state["consulting"] = False


def _render_fallback(scene_id: int):
    """渲染降级静态内容"""
    fallback = FALLBACK_CONTENT.get(scene_id, {})
    if not fallback:
        st.error("暂无通用建议")
        return

    title = get_fallback_title()
    st.warning(title)

    content = fallback.get("content", "")
    if is_xianxia():
        from utils.theme import get_xianxia_terms_text
        content = get_xianxia_terms_text(content)

    st.markdown(content)
    render_disclaimer(scene_id)


def render_scene(scene_id: int, api_url: str, api_key: str, model_name: str):
    """渲染完整的场景页面（输入+输出）"""
    # 如果正在咨询中，禁止切换场景
    if st.session_state.get("consulting", False):
        st.warning(get_consulting_text())
        return

    user_inputs = render_scene_input(scene_id)

    st.markdown("---")

    # 验证并提交
    is_valid, errors = validate_inputs(scene_id, user_inputs)
    if errors:
        for err in errors:
            st.error(err)

    render_scene_output(scene_id, user_inputs, api_url, api_key, model_name)
