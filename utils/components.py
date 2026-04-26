"""
职场修仙大护法 - 通用UI组件
"""

import os

import streamlit as st
from utils.config import GENERAL_DISCLAIMER, SCENE4_DISCLAIMER
from utils.theme import get_ai_name, is_xianxia, get_status_online, get_status_offline


def render_status_indicator(is_online: bool):
    """渲染大护法在线状态指示器"""
    online_text, offline_text = get_status_online()
    if is_online:
        st.markdown(
            f'<span style="display:inline-flex;align-items:center;gap:6px;'
            f'color:#27ae60;font-size:14px;font-weight:600;">'
            f'<span style="width:8px;height:8px;border-radius:50%;background:#27ae60;'
            f'display:inline-block;animation:pulse 2s infinite;"></span>'
            f'{online_text}</span>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<span style="display:inline-flex;align-items:center;gap:6px;'
            f'color:#95a5a6;font-size:14px;">'
            f'<span style="width:8px;height:8px;border-radius:50%;background:#95a5a6;'
            f'display:inline-block;"></span>'
            f'{offline_text}</span>',
            unsafe_allow_html=True
        )


def render_disclaimer(scene_id: int = None):
    """渲染免责声明"""
    st.markdown("---")
    st.caption(GENERAL_DISCLAIMER)
    if scene_id == 4:
        st.markdown(
            f'<p style="color:#e74c3c;font-weight:600;font-size:13px;'
            f'border-left:3px solid #e74c3c;padding-left:10px;margin-top:8px;">'
            f'{SCENE4_DISCLAIMER}</p>',
            unsafe_allow_html=True
        )


def render_api_config_sidebar():
    """渲染侧边栏API配置表单，返回 (api_url, api_key, model_name)"""
    with st.sidebar:
        st.header("⚙️ API 配置")

        # 检查环境变量是否已配置（适配 Streamlit Cloud 云端部署）
        env_url = os.environ.get("API_URL", "")
        env_key = os.environ.get("API_KEY", "")
        env_model = os.environ.get("MODEL_NAME", "")
        has_env = bool(env_url and env_key and env_model)

        if has_env:
            # 环境变量已配置，直接使用，不显示输入框
            st.info("✅ API 已通过环境变量配置，无需手动设置")

            api_url = env_url
            api_key = env_key
            model_name = env_model

            # 更新 session_state
            st.session_state.api_url = api_url
            st.session_state.api_key = api_key
            st.session_state.model_name = model_name

            # 首次自动测试连通性（不阻塞页面渲染）
            if not st.session_state.get("api_tested"):
                with st.spinner("正在检测 API 连通性..."):
                    from utils.api_client import test_connection
                    try:
                        success, message = test_connection(api_url, api_key, model_name)
                        st.session_state.api_online = success
                        if success:
                            st.success(f"✅ {message}")
                        else:
                            st.error(f"❌ {message}")
                    except Exception as e:
                        st.session_state.api_online = False
                        st.error(f"❌ 连接检测失败：{str(e)[:80]}")
                st.session_state.api_tested = True

            # 手动重新测试按钮
            if st.button("🔄 重新测试连接", use_container_width=True):
                with st.spinner("正在测试连接..."):
                    from utils.api_client import test_connection
                    success, message = test_connection(api_url, api_key, model_name)
                    if success:
                        st.success(message)
                        st.session_state.api_online = True
                    else:
                        st.error(message)
                        st.session_state.api_online = False

            # 底部免责声明
            st.sidebar.markdown("---")
            st.sidebar.caption("⚠️ 本内容由AI生成，仅供参考，不构成专业建议。")
            st.sidebar.caption("请结合自身实际情况做出判断和决策。")

            return api_url, api_key, model_name

        # 环境变量未配置，显示手动输入表单
        st.warning("⚠️ 未检测到环境变量配置，请手动填写 API 信息")

        # 从session_state加载已有配置
        if "api_url" not in st.session_state:
            st.session_state.api_url = ""
        if "api_key" not in st.session_state:
            st.session_state.api_key = ""
        if "model_name" not in st.session_state:
            st.session_state.model_name = ""

        api_url = st.text_input(
            "API 地址",
            value=st.session_state.api_url,
            placeholder="如：https://api.deepseek.com/v1",
            key="config_api_url",
            help="OpenAI 兼容 API 的 Base URL"
        )
        api_key = st.text_input(
            "API Key",
            value=st.session_state.api_key,
            type="password",
            placeholder="sk-...",
            key="config_api_key",
            help="你的 API 密钥"
        )
        model_name = st.text_input(
            "模型名称",
            value=st.session_state.model_name,
            placeholder="如：deepseek-chat",
            key="config_model_name",
            help="模型标识"
        )

        # 保存到session_state
        st.session_state.api_url = api_url
        st.session_state.api_key = api_key
        st.session_state.model_name = model_name

        # 测试连接按钮
        if st.button("🔗 测试连接", use_container_width=True):
            if not api_url or not api_key or not model_name:
                st.error("请填写完整的 API 配置信息")
            else:
                with st.spinner("正在测试连接..."):
                    from utils.api_client import test_connection
                    success, message = test_connection(api_url, api_key, model_name)
                    if success:
                        st.success(message)
                        st.session_state.api_online = True
                    else:
                        st.error(message)
                        st.session_state.api_online = False

        # 保存到localStorage
        if api_url or api_key or model_name:
            from utils.history import save_config
            save_config(api_url, api_key, model_name)

        # 底部免责声明
        st.sidebar.markdown("---")
        st.sidebar.caption("⚠️ 本内容由AI生成，仅供参考，不构成专业建议。")
        st.sidebar.caption("请结合自身实际情况做出判断和决策。")

    return api_url, api_key, model_name


def render_example_questions(scene_id: int):
    """渲染示例问题折叠面板"""
    from utils.config import SCENES
    scene = SCENES.get(scene_id, {})
    examples = scene.get("example_questions", [])
    if not examples:
        return

    with st.expander("💡 不知道怎么描述？点击查看示例"):
        for i, q in enumerate(examples, 1):
            if st.button(f"示例{i}：{q[:30]}{'...' if len(q) > 30 else ''}",
                        key=f"example_{scene_id}_{i}", use_container_width=True):
                # 找到textarea字段并预填充
                from utils.config import SCENES
                schema = scene.get("inputs_schema", [])
                for field in schema:
                    if field["type"] == "textarea" and field.get("required", False):
                        st.session_state[f"input_{field['key']}"] = q
                        st.info(f"已填入示例，你可以修改后提交")
                        break


def render_scene_selector() -> int:
    """渲染场景选择器，返回选中的场景ID"""
    from utils.config import SCENES
    from utils.theme import get_scene_name, get_scene_icon

    cols = st.columns(4)
    selected = st.session_state.get("current_scene", 1)

    for i, (scene_id, scene) in enumerate(SCENES.items()):
        col = cols[i % 4]
        name = get_scene_name(scene_id)
        icon = get_scene_icon(scene_id)
        is_selected = (scene_id == selected)

        button_style = (
            "border:2px solid #1B4F72;background:#EBF5FB;" if is_selected
            else "border:1px solid #ddd;background:#fff;"
        )
        label = f"{icon} {name}"

        with col:
            if st.button(label, key=f"scene_{scene_id}", use_container_width=True):
                st.session_state.current_scene = scene_id
                st.rerun()

    return st.session_state.get("current_scene", 1)


def render_history_panel():
    """渲染历史记录面板"""
    from utils.history import get_history, delete_history, clear_history, toggle_star
    from utils.theme import is_xianxia

    st.sidebar.markdown("---")
    st.sidebar.header("📜 历史记录")

    history = get_history()

    if not history:
        st.sidebar.caption("暂无历史记录")
        return

    # 搜索框
    search = st.sidebar.text_input("🔍 搜索", placeholder="搜索场景名、输入内容、AI输出...", key="history_search")

    # 筛选
    filtered = history
    if search:
        from utils.history import search_history
        filtered = search_history(search)

    # 收藏筛选
    show_starred = st.sidebar.checkbox("⭐ 仅显示收藏", key="show_starred")
    if show_starred:
        filtered = [r for r in filtered if r.get("starred")]

    st.sidebar.caption(f"共 {len(filtered)} 条记录")
    st.sidebar.caption("📦 最多保存200条记录，超出自动清理旧记录")

    # 操作按钮
    col1, col2 = st.sidebar.columns(2)
    with col1:
        if st.button("🗑️ 清空", use_container_width=True):
            clear_history()
            st.rerun()
    with col2:
        # 直接导出全部
        if filtered:
            export_parts = []
            for r in filtered:
                export_parts.append(f"=== {r.get('scene_name', '')} - {r.get('timestamp', '')} ===")
                ui = r.get("user_input", {})
                if isinstance(ui, dict):
                    for k, v in ui.items():
                        if v and v != "未提供":
                            export_parts.append(f"  {k}: {v}")
                else:
                    export_parts.append(f"  输入: {ui}")
                export_parts.append("")
                export_parts.append(r.get("ai_output", ""))
                export_parts.append("\n" + "=" * 50 + "\n")
            export_content = "\n".join(export_parts)
            st.sidebar.download_button(
                label="📤 导出全部",
                data=export_content,
                file_name="大护法_全部历史记录.txt",
                mime="text/plain",
                use_container_width=True,
            )

    # 记录列表
    for record in filtered[:20]:  # 最多显示20条
        record_id = record.get("id", 0)
        scene_name = record.get("scene_name", "未知场景")
        timestamp = record.get("timestamp", "")
        starred = record.get("starred", False)
        star_icon = "⭐" if starred else "☆"

        with st.sidebar.expander(f"{star_icon} {scene_name} - {timestamp}"):
            # 用户输入摘要
            user_input = record.get("user_input", {})
            if isinstance(user_input, dict):
                input_preview = " | ".join(
                    f"{k}: {str(v)[:20]}" for k, v in user_input.items() if v and v != "未提供"
                )
            else:
                input_preview = str(user_input)[:50]
            st.caption(f"📝 {input_preview}")

            # AI输出预览
            ai_output = record.get("ai_output", "")
            st.markdown(ai_output)

            # 操作按钮：收藏、删除（同行显示）
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("⭐" if not starred else "取消⭐",
                           key=f"star_{record_id}", use_container_width=True):
                    toggle_star(record_id)
                    st.rerun()
            with col_b:
                if st.button("🗑️", key=f"del_{record_id}", use_container_width=True):
                    delete_history(record_id)
                    st.rerun()


def render_mobile_css():
    """注入移动端适配CSS + 双模式差异化样式"""
    from utils.theme import is_xianxia
    
    if is_xianxia():
        # 修仙模式 - 淡紫色古风主题
        st.markdown("""
        <style>
        /* 修仙模式全局背景 - 淡紫色 */
        .stApp {
            background: linear-gradient(160deg, #f3e8ff 0%, #ede9fe 40%, #e8e0f7 100%) !important;
        }
        /* 标题颜色 */
        h1, h2, h3, .stTitle {
            color: #5b21b6 !important;
        }
        /* 正文颜色 - 深色确保可读 */
        .stMarkdown, .stCaption, p, span, label {
            color: #3b0764 !important;
        }
        /* 输入框 - 白底深色文字，清晰可读 */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {
            background-color: #ffffff !important;
            color: #1e1b4b !important;
            border: 1px solid #c4b5fd !important;
            border-radius: 8px !important;
        }
        /* 主按钮 - 紫色渐变 */
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #a78bfa, #7c3aed) !important;
            border: none !important;
            color: white !important;
        }
        /* 普通按钮 */
        .stButton > button:not([kind="primary"]) {
            background: rgba(124, 58, 237, 0.08) !important;
            border: 1px solid #c4b5fd !important;
            color: #5b21b6 !important;
        }
        .stButton > button:not([kind="primary"]):hover {
            background: rgba(124, 58, 237, 0.18) !important;
        }
        /* 侧边栏 - 浅紫 */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #ede9fe 0%, #f3e8ff 100%) !important;
        }
        [data-testid="stSidebar"] .stMarkdown,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] label {
            color: #3b0764 !important;
        }
        /* 表格边框可见 */
        th, td {
            border: 1px solid #c4b5fd !important;
            color: #1e1b4b !important;
        }
        thead th {
            background-color: #ddd6fe !important;
            color: #4c1d95 !important;
        }
        tr:nth-child(even) {
            background-color: #f5f3ff !important;
        }
        /* expander */
        .stExpander {
            border: 1px solid #c4b5fd !important;
            border-radius: 8px !important;
        }
        /* alert */
        .stAlert {
            background: rgba(167, 139, 250, 0.15) !important;
            border-left: 3px solid #8b5cf6 !important;
        }
        /* 按钮圆角 */
        .stButton > button {
            border-radius: 8px !important;
        }
        /* 移动端适配 */
        @media (max-width: 768px) {
            .stTextInput > div > div > input,
            .stTextArea > div > div > textarea,
            .stSelectbox > div > div > select {
                font-size: 16px !important;
            }
            div[data-testid="stSidebar"] {
                width: 100% !important;
            }
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        # 职场模式 - 保持默认现代简约风格
        st.markdown("""
        <style>
        @media (max-width: 768px) {
            .stTextInput > div > div > input,
            .stTextArea > div > div > textarea,
            .stSelectbox > div > div > select {
                font-size: 16px !important;
            }
            div[data-testid="stSidebar"] {
                width: 100% !important;
            }
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        </style>
        """, unsafe_allow_html=True)


def render_first_time_guide():
    """渲染首次用户引导流程"""
    from utils.config import SCENES
    from utils.theme import get_scene_name, get_scene_icon

    if st.session_state.get("guide_step") is None:
        st.session_state.guide_step = 0

    step = st.session_state.guide_step

    if step == 0:
        # 步骤1：欢迎
        st.markdown("## 🎮 欢迎来到职场修仙大护法")
        st.markdown("""
        > 职场如修仙，每一次"新"都是一次渡劫。
        > 大护法将助你化解职场八大劫难！

        在开始之前，请先配置你的 AI 模型。
        """)
        if st.button("✅ 已配置好API，下一步", type="primary", use_container_width=True):
            if st.session_state.get("api_url") and st.session_state.get("api_key"):
                st.session_state.guide_step = 1
                st.rerun()
            else:
                st.warning("请先在左侧配置 API 信息并测试连接")

    elif step == 1:
        # 步骤2：选择场景
        st.markdown('## 🎯 选择你正在经历的"劫难"')
        st.caption("点击选择一个场景，大护法将为你量身定制攻略")

        cols = st.columns(2)
        for i, (scene_id, scene) in enumerate(SCENES.items()):
            col = cols[i % 2]
            name = get_scene_name(scene_id)
            icon = get_scene_icon(scene_id)
            desc = scene.get("description", "")[:30] + "..."

            with col:
                if st.button(f"{icon} **{name}**\n\n{desc}",
                           key=f"guide_scene_{scene_id}", use_container_width=True):
                    st.session_state.current_scene = scene_id
                    st.session_state.guide_step = 2
                    st.rerun()

    elif step == 2:
        # 步骤3：示例引导
        scene_id = st.session_state.get("current_scene", 1)
        scene = SCENES.get(scene_id, {})
        name = get_scene_name(scene_id)
        icon = get_scene_icon(scene_id)

        st.markdown(f"## {icon} {name}")
        st.markdown("你可以参考以下示例来描述你的情况：")
        render_example_questions(scene_id)

        if st.button("🚀 开始咨询", type="primary", use_container_width=True):
            st.session_state.guide_step = -1  # 引导完成
            st.rerun()

        if st.button("↩️ 返回选择场景"):
            st.session_state.guide_step = 1
            st.rerun()
