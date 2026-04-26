"""
职场修仙大护法 - 历史记录管理
通过 JS 注入实现 localStorage 读写。
适配 Streamlit 1.56+（使用 st.iframe 替代已弃用的 st.components.v1.html）
"""

import json
import time
import streamlit as st
from utils.config import STORAGE_KEY_HISTORY, STORAGE_KEY_CONFIG, STORAGE_KEY_THEME


def _inject_js(code: str):
    """注入 JS 代码（不阻塞渲染，用于写入操作）"""
    st.markdown(f"""
    <script>{code}</script>
    """, unsafe_allow_html=True)


def _read_localstorage(key: str):
    """从 localStorage 读取值（使用 st.iframe，适配 Streamlit 1.56+）"""
    html = f"""
    <html><body><script>
    try {{
        var val = localStorage.getItem('{key}');
        window.parent.postMessage({{
            type: 'streamlit:setComponentValue',
            value: val
        }}, '*');
    }} catch(e) {{
        window.parent.postMessage({{
            type: 'streamlit:setComponentValue',
            value: null
        }}, '*');
    }}
    </script></body></html>
    """
    return st.iframe(html, height=0)


def save_config(api_url: str, api_key: str, model_name: str):
    """保存API配置到localStorage"""
    config = {"api_url": api_url, "api_key": api_key, "model_name": model_name}
    config_json = json.dumps(config, ensure_ascii=False)
    _inject_js(f"localStorage.setItem('{STORAGE_KEY_CONFIG}', '{config_json}');")


def load_config():
    """从localStorage加载API配置"""
    result = _read_localstorage(STORAGE_KEY_CONFIG)
    if result and isinstance(result, str):
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            return None
    return None


def save_theme(theme: str):
    """保存主题模式到localStorage"""
    _inject_js(f"localStorage.setItem('{STORAGE_KEY_THEME}', '{theme}');")


def load_theme():
    """从localStorage加载主题模式"""
    result = _read_localstorage(STORAGE_KEY_THEME)
    if result and isinstance(result, str):
        return result
    return None


def add_history(scene_id: int, scene_name: str, user_input: dict,
                ai_output: str, theme_mode: str):
    """添加一条历史记录"""
    record = {
        "id": int(time.time() * 1000),
        "scene_id": scene_id,
        "scene_name": scene_name,
        "user_input": user_input,  # 存全量
        "ai_output": ai_output,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "theme_mode": theme_mode,
        "starred": False,
    }
    # 获取现有记录
    history = get_history()
    history.insert(0, record)  # 最新的在前面
    # 限制最多200条
    if len(history) > 200:
        history = history[:200]
    # 保存
    _save_history(history)


def get_history() -> list:
    """获取所有历史记录"""
    if "history" not in st.session_state:
        st.session_state.history = []
    return st.session_state.history


def _save_history(history: list):
    """保存历史记录到session_state（localStorage由前端定期同步）"""
    st.session_state.history = history
    # 尝试保存到localStorage
    try:
        history_json = json.dumps(history, ensure_ascii=False)
        # localStorage有5MB限制，单条记录截断保护
        if len(history_json) > 4 * 1024 * 1024:  # 4MB
            # 删除最早的20条
            history = history[20:]
            history_json = json.dumps(history, ensure_ascii=False)
            st.session_state.history = history
        _inject_js(f"localStorage.setItem('{STORAGE_KEY_HISTORY}', '{history_json}');")
    except Exception:
        pass  # localStorage不可用时仅保存在session_state


def load_history_from_storage():
    """从localStorage加载历史记录到session_state"""
    result = _read_localstorage(STORAGE_KEY_HISTORY)
    if result and isinstance(result, str):
        try:
            history = json.loads(result)
            if isinstance(history, list):
                st.session_state.history = history
        except json.JSONDecodeError:
            st.session_state.history = []


def delete_history(record_id: int):
    """删除单条历史记录"""
    history = get_history()
    history = [r for r in history if r.get("id") != record_id]
    _save_history(history)


def clear_history():
    """清空所有历史记录"""
    st.session_state.history = []
    _inject_js(f"localStorage.removeItem('{STORAGE_KEY_HISTORY}');")


def toggle_star(record_id: int):
    """切换收藏状态"""
    history = get_history()
    for r in history:
        if r.get("id") == record_id:
            r["starred"] = not r["starred"]
            break
    _save_history(history)


def search_history(keyword: str) -> list:
    """搜索历史记录"""
    history = get_history()
    if not keyword:
        return history
    keyword = keyword.lower()
    return [
        r for r in history
        if keyword in r.get("scene_name", "").lower()
        or keyword in str(r.get("user_input", "")).lower()
        or keyword in r.get("ai_output", "").lower()
    ]
