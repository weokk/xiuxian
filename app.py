"""
职场修仙大护法 - 主应用入口
"""

import os

import streamlit as st

# st.set_page_config 必须是第一条 Streamlit 命令
st.set_page_config(
    page_title="职场修仙大护法",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded",
)

from utils.config import APP_NAME, APP_VERSION, SCENES
from utils.theme import (
    get_theme, set_theme, toggle_theme, is_xianxia,
    get_ai_name, get_theme_emoji, get_theme_label,
    get_scene_name, get_scene_icon,
)
from utils.components import (
    render_status_indicator, render_api_config_sidebar,
    render_scene_selector, render_history_panel,
    render_mobile_css, render_first_time_guide,
)
from utils.scene_handlers import render_scene
from utils.history import load_history_from_storage, load_config, load_theme, save_theme


def init_session_state():
    """初始化session_state"""
    defaults = {
        "current_scene": 1,
        "api_online": False,
        "consulting": False,
        "last_consult_time": 0,
        "guide_step": None,
        "api_url": "",
        "api_key": "",
        "model_name": "",
        "env_config": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def load_saved_config():
    """从localStorage加载已保存的配置（仅首次加载时执行）"""
    if st.session_state.get("config_loaded"):
        return

    # 优先检查环境变量（适配 Streamlit Cloud 部署）
    env_api_url = os.environ.get("API_URL", "")
    env_api_key = os.environ.get("API_KEY", "")
    env_model_name = os.environ.get("MODEL_NAME", "")

    if env_api_url and env_api_key and env_model_name:
        st.session_state.api_url = env_api_url
        st.session_state.api_key = env_api_key
        st.session_state.model_name = env_model_name
        st.session_state.env_config = True

        # 加载主题
        saved_theme = load_theme()
        if saved_theme in ("xianxia", "workplace"):
            set_theme(saved_theme)

        # 加载历史记录
        load_history_from_storage()

        st.session_state.config_loaded = True
        return

    # 加载API配置
    saved_config = load_config()
    if saved_config:
        st.session_state.api_url = saved_config.get("api_url", "")
        st.session_state.api_key = saved_config.get("api_key", "")
        st.session_state.model_name = saved_config.get("model_name", "")

    # 加载主题
    saved_theme = load_theme()
    if saved_theme in ("xianxia", "workplace"):
        set_theme(saved_theme)

    # 加载历史记录
    load_history_from_storage()

    st.session_state.config_loaded = True


def main():
    # 初始化
    init_session_state()

    # 注入移动端CSS
    render_mobile_css()

    # 加载已保存的配置
    load_saved_config()

    # ===== 侧边栏 =====
    api_url, api_key, model_name = render_api_config_sidebar()
    render_history_panel()

    # ===== 顶部导航栏 =====
    ai_name = get_ai_name()

    # 标题 + 模式开关 + 状态
    col_title, col_switch, col_status = st.columns([3, 2, 1])

    with col_title:
        st.title(f"⚔️ {APP_NAME}")

    with col_switch:
        st.markdown("<br>", unsafe_allow_html=True)
        current = get_theme()
        # 用radio同时显示两个选项，只能选一个
        mode_choice = st.radio(
            "模式选择",
            options=["xianxia", "workplace"],
            format_func=lambda x: "⚔️ 修仙模式" if x == "xianxia" else "💼 职场模式",
            index=0 if current == "xianxia" else 1,
            horizontal=True,
            key="mode_radio",
            label_visibility="collapsed",
        )
        if mode_choice != current:
            set_theme(mode_choice)
            save_theme(mode_choice)
            st.rerun()

    with col_status:
        st.markdown("<br>", unsafe_allow_html=True)
        render_status_indicator(st.session_state.get("api_online", False))

    st.caption(f"版本 {APP_VERSION}")

    st.markdown("---")

    # ===== 首次引导检查 =====
    history = st.session_state.get("history", [])
    has_config = bool(st.session_state.get("api_url") and st.session_state.get("api_key"))

    if not history and not has_config and not st.session_state.get("env_config"):
        # 首次使用，显示引导
        render_first_time_guide()
        return

    # ===== 场景选择 =====
    scene_id = render_scene_selector()

    st.markdown("---")

    # ===== 场景内容 =====
    render_scene(scene_id, api_url, api_key, model_name)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"应用运行出错：{e}")
        import traceback
        st.code(traceback.format_exc())
