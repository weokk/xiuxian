"""
职场修仙大护法 - 双模式主题管理
"""

import streamlit as st

from utils.config import THEME_XIANXIA, THEME_WORKPLACE, SCENES, XIANXIA_TERMS


def get_theme():
    """获取当前主题模式"""
    if "theme" not in st.session_state:
        st.session_state.theme = THEME_WORKPLACE
    return st.session_state.theme


def set_theme(theme):
    """设置主题模式"""
    st.session_state.theme = theme


def toggle_theme():
    """切换主题模式"""
    current = get_theme()
    new_theme = THEME_XIANXIA if current == THEME_WORKPLACE else THEME_WORKPLACE
    set_theme(new_theme)
    return new_theme


def is_xianxia():
    """判断当前是否为修仙模式"""
    return get_theme() == THEME_XIANXIA


def get_scene_name(scene_id):
    """获取当前主题下的场景名称"""
    scene = SCENES.get(scene_id, {})
    if is_xianxia():
        return scene.get("xianxia_name", scene.get("name", ""))
    return scene.get("name", "")


def get_scene_icon(scene_id):
    """获取当前主题下的场景图标"""
    scene = SCENES.get(scene_id, {})
    if is_xianxia():
        return scene.get("xianxia_icon", scene.get("icon", "📌"))
    return scene.get("icon", "📌")


def get_ai_name():
    """获取当前主题下的AI称呼"""
    return "大护法" if is_xianxia() else "AI职场顾问"


def get_status_online():
    """获取在线状态文案"""
    if is_xianxia():
        return "大护法在线", "大护法闭关中"
    return "AI顾问在线", "AI顾问离线"


def get_status_offline():
    """获取离线状态文案"""
    if is_xianxia():
        return "大护法闭关中"
    return "AI顾问离线"


def get_consulting_text():
    """获取咨询中提示文案"""
    if is_xianxia():
        return "大护法正在为你出谋划策，请稍候..."
    return "AI顾问正在分析中，请稍候..."


def get_fallback_title():
    """获取降级内容标题"""
    if is_xianxia():
        return "大护法暂时无法施展法力，以下为通用修炼秘籍供参考"
    return "AI顾问暂时不可用，以下为通用职场建议供参考"


def get_theme_emoji():
    """获取主题切换按钮文案"""
    if is_xianxia():
        return "🔄 切换到职场模式"
    return "🔄 切换到修仙模式"


def get_theme_label():
    """获取当前主题标签"""
    return "修仙模式" if is_xianxia() else "职场模式"


def get_xianxia_terms_text(text):
    """将职场术语替换为修仙术语（仅在修仙模式下使用）"""
    if not is_xianxia():
        return text
    result = text
    for workplace, xianxia in XIANXIA_TERMS.items():
        result = result.replace(workplace, xianxia)
    return result
