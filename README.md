# 🧙‍♂️ 职场修仙大护法



一款以修仙/仙侠游戏隐喻包装的职场生存 AI 工具，帮助职场新人轻松应对各种"渡劫"场景。

---

## 📖 项目简介

职场修仙大护法将职场新人的常见困境映射为修仙世界中的"渡劫"关卡，通过 AI 驱动的智能对话，为用户提供沉浸式、场景化的职场建议与指导。

无论你是初入职场的新人，还是面临团队管理挑战的职场老手，大护法都能为你指点迷津，助你在职场修仙路上稳步前行。

---

## ✨ 功能特性

### 🎮 双主题模式
- **修仙模式** — 淡紫色古风主题，沉浸式仙侠体验
- **职场模式** — 简约白色主题，专注高效办公

### 🏔️ 八大渡劫场景
| 场景 | 修仙隐喻 | 说明 |
|------|---------|------|
| 新人入职 | 初入仙门 | 入职指南与注意事项 |
| 融入新团队 | 结交道友 | 快速融入团队的方法与技巧 |
| 接受新项目 | 接受宗门任务 | 项目承接与规划建议 |
| 适应新领导 | 适应新掌门 | 向上管理与沟通策略 |
| 组织新变革 | 宗门大变革 | 应对组织架构调整 |
| 快学新东西 | 修炼新功法 | 快速学习新技能的方法论 |
| 新带团队 | 收徒传道 | 团队管理入门与实践 |
| 新负责项目 | 镇守新秘境 | 项目管理全流程指导 |

### 🤖 AI 智能对话
- 支持任何 **OpenAI 兼容 API**（DeepSeek、通义千问、智谱等）
- 🔄 **流式输出**，打字机效果，实时呈现 AI 回复
- 💬 **多轮对话**，上下文连贯

### 📜 历史记录
- ⭐ 收藏精彩回答
- 🔍 搜索历史对话
- 🗑️ 一键清空记录

### 📱 移动端适配
- 响应式布局，手机、平板、桌面均可流畅使用

---

## 🛠️ 技术栈

| 技术 | 版本要求 |
|------|---------|
| Python | >= 3.10 |
| Streamlit | >= 1.40.0 |
| OpenAI Python SDK | >= 1.50.0 |
| httpx | >= 0.27.0 |

---

## 🚀 部署方式

### ☁️ Streamlit Cloud 部署（推荐）

1. **Fork 或 Clone** 本仓库
2. 在 Streamlit Cloud 的 **Secrets** 中配置以下环境变量：

   ```toml
   API_URL = "https://api.example.com/v1"
   API_KEY = "sk-xxxxxxxxxxxxxxxx"
   MODEL_NAME = "deepseek-chat"
   ```

3. 设置主文件路径为 `app.py`，点击 **Deploy** 即可

### 💻 本地运行

1. **安装依赖**

   ```bash
   pip install -r requirements.txt
   ```

2. **配置 API**

   方式一：设置环境变量

   ```bash
   export API_URL="https://api.example.com/v1"
   export API_KEY="sk-xxxxxxxxxxxxxxxx"
   export MODEL_NAME="deepseek-chat"
   ```

   方式二：在应用界面侧边栏手动配置

3. **启动应用**

   ```bash
   streamlit run app.py
   ```

---

## 📁 目录结构

```
deploy/
├── app.py                  # 应用主入口
├── requirements.txt        # Python 依赖
├── README.md               # 项目说明文档
└── utils/
    ├── __init__.py
    ├── api_client.py       # OpenAI 兼容 API 客户端
    ├── components.py       # Streamlit UI 组件
    ├── config.py           # 配置管理
    ├── history.py          # 历史记录管理
    ├── prompts.py          # 提示词模板
    ├── scene_handlers.py   # 场景处理器
    ├── theme.py            # 主题切换逻辑
    └── data/               # 场景数据
        ├── __init__.py
        ├── fallback.py          # 兜底回复
        ├── fast_learning.py     # 快学新东西
        ├── new_leader.py        # 适应新领导
        ├── new_project.py       # 接受新项目
        ├── onboarding.py        # 新人入职
        ├── org_change.py        # 组织新变革
        ├── project_managing.py  # 新负责项目
        ├── team_integration.py  # 融入新团队
        └── team_leading.py      # 新带团队
```

---

## 📸 截图预览

<!-- 修仙模式截图 -->
| 修仙模式 | 职场模式 |
|:---:|:---:|
| ![修仙模式](screenshots/cultivation-mode.png) | ![职场模式](screenshots/workplace-mode.png) |

<!-- 移动端截图 -->
| 移动端适配 |
|:---:|
| ![移动端](screenshots/mobile-view.png) |

> 📌 截图待补充，部署后可替换为实际截图。

---

## 📄 许可证

本项目基于 [MIT License](LICENSE) 开源。


---

# 🧙‍♂️ Workplace Cultivation Guardian (职场修仙大护法)

> Entry for TRAE × Maimai "AI Infinite Workplace" SOLO Challenge

An AI-powered workplace survival tool wrapped in a cultivation (xianxia) game metaphor, helping workplace newcomers navigate various "tribulation" scenarios with ease.

---

## 📖 Overview

Workplace Cultivation Guardian maps common workplace challenges for newcomers to "tribulation" levels in a cultivation world. Through AI-driven intelligent conversations, it provides users with immersive, scenario-based workplace advice and guidance.

Whether you are a newcomer just entering the workplace or an experienced professional facing team management challenges, the Guardian can point you in the right direction and help you progress steadily on your workplace cultivation journey.

---

## ✨ Features

### 🎮 Dual Theme Modes
- **Cultivation Mode** — Purple-toned ancient Chinese aesthetic for an immersive xianxia experience
- **Workplace Mode** — Clean white minimalist theme for focused productivity

### 🏔️ Eight Tribulation Scenarios
| Scenario | Cultivation Metaphor | Description |
|----------|---------------------|-------------|
| New Onboarding | Entering the Sect | Onboarding guide and key points |
| Team Integration | Making Fellow Cultivators | Tips for quickly integrating into a team |
| New Project Assignment | Accepting Sect Missions | Project planning and execution advice |
| Adapting to New Leadership | Adapting to a New Sect Master | Upward management and communication strategies |
| Organizational Change | Great Sect Reform | Navigating organizational restructuring |
| Fast Learning | Cultivating New Techniques | Methodologies for rapid skill acquisition |
| Team Leadership | Taking on Disciples | Team management fundamentals and practice |
| Project Management | Guarding a New Secret Realm | End-to-end project management guidance |

### 🤖 AI-Powered Conversations
- Compatible with any **OpenAI-compatible API** (DeepSeek, Tongyi Qianwen, Zhipu, etc.)
- 🔄 **Streaming output** with typewriter effect for real-time AI responses
- 💬 **Multi-turn conversations** with contextual continuity

### 📜 Conversation History
- ⭐ Bookmark insightful responses
- 🔍 Search through conversation history
- 🗑️ Clear all history with one click

### 📱 Mobile Responsive
- Responsive layout that works seamlessly on phones, tablets, and desktops

---

## 🛠️ Tech Stack

| Technology | Version |
|------------|---------|
| Python | >= 3.10 |
| Streamlit | >= 1.40.0 |
| OpenAI Python SDK | >= 1.50.0 |
| httpx | >= 0.27.0 |

---

## 🚀 Deployment

### ☁️ Streamlit Cloud (Recommended)

1. **Fork or Clone** this repository
2. Configure the following environment variables in Streamlit Cloud **Secrets**:

   ```toml
   API_URL = "https://api.example.com/v1"
   API_KEY = "sk-xxxxxxxxxxxxxxxx"
   MODEL_NAME = "deepseek-chat"
   ```

3. Set the main file path to `app.py` and click **Deploy**

### 💻 Local Development

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API**

   Option A: Set environment variables

   ```bash
   export API_URL="https://api.example.com/v1"
   export API_KEY="sk-xxxxxxxxxxxxxxxx"
   export MODEL_NAME="deepseek-chat"
   ```

   Option B: Configure manually in the app sidebar

3. **Launch the app**

   ```bash
   streamlit run app.py
   ```

---

## 📁 Project Structure

```
deploy/
├── app.py                  # Application entry point
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── utils/
    ├── __init__.py
    ├── api_client.py       # OpenAI-compatible API client
    ├── components.py       # Streamlit UI components
    ├── config.py           # Configuration management
    ├── history.py          # Conversation history management
    ├── prompts.py          # Prompt templates
    ├── scene_handlers.py   # Scene handlers
    ├── theme.py            # Theme switching logic
    └── data/               # Scene data
        ├── __init__.py
        ├── fallback.py          # Fallback responses
        ├── fast_learning.py     # Fast learning scenario
        ├── new_leader.py        # New leadership scenario
        ├── new_project.py       # New project scenario
        ├── onboarding.py        # Onboarding scenario
        ├── org_change.py        # Organizational change scenario
        ├── project_managing.py  # Project management scenario
        ├── team_integration.py  # Team integration scenario
        └── team_leading.py      # Team leadership scenario
```

---

## 📸 Screenshots

<!-- Cultivation Mode Screenshot -->
| Cultivation Mode | Workplace Mode |
|:---:|:---:|
| ![Cultivation Mode](screenshots/cultivation-mode.png) | ![Workplace Mode](screenshots/workplace-mode.png) |

<!-- Mobile Screenshot -->
| Mobile Responsive |
|:---:|
| ![Mobile View](screenshots/mobile-view.png) |

> 📌 Screenshots to be added after deployment.

---

## 📄 License

This project is open-sourced under the [MIT License](LICENSE).

---


