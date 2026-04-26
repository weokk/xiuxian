"""
职场修仙大护法 - 历史记录管理
使用纯 session_state 管理状态（兼容 Streamlit Cloud）。
localStorage 相关功能已移除，避免 st.iframe/st.components.v1.html 兼容性问题。
"""

import json
import time
import streamlit as st
from utils.config import STORAGE_KEY_HISTORY, STORAGE_KEY_CONFIG, STORAGE_KEY_THEME


def save_config(api_url: str, api_key: str, model_name: str):
    """保存API配置到session_state"""
    st.session_state.api_url = api_url
    st.session_state.api_key = api_key
    st.session_state.model_name = model_name


def load_config():
    """从session_state加载API配置"""
    api_url = st.session_state.get("api_url", "")
    api_key = st.session_state.get("api_key", "")
    model_name = st.session_state.get("model_name", "")
    if api_url or api_key or model_name:
        return {"api_url": api_url, "api_key": api_key, "model_name": model_name}
    return None


def save_theme(theme: str):
    """保存主题模式到session_state"""
    st.session_state["_theme"] = theme


def load_theme():
    """从session_state加载主题模式"""
    return st.session_state.get("_theme")


def add_history(scene_id: int, scene_name: str, user_input: dict,
                ai_output: str, theme_mode: str):
    """添加一条历史记录"""
    record = {
        "id": int(time.time() * 1000),
        "scene_id": scene_id,
        "scene_name": scene_name,
        "user_input": user_input,
        "ai_output": ai_output,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "theme_mode": theme_mode,
        "starred": False,
    }
    history = get_history()
    history.insert(0, record)
    # 限制最多200条
    if len(history) > 200:
        history = history[:200]
    st.session_state.history = history


def get_history() -> list:
    """获取所有历史记录"""
    if "history" not in st.session_state:
        st.session_state.history = []
    return st.session_state.history


def _save_history(history: list):
    """保存历史记录到session_state"""
    st.session_state.history = history


def load_history_from_storage():
    """加载历史记录（从session_state，兼容旧接口）"""
    if "history" not in st.session_state:
        st.session_state.history = []


def delete_history(record_id: int):
    """删除单条历史记录"""
    history = get_history()
    history = [r for r in history if r.get("id") != record_id]
    _save_history(history)


def clear_history():
    """清空所有历史记录"""
    st.session_state.history = []


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
