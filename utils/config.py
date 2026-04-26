"""
职场修仙大护法 - 场景定义与常量配置
"""

# 应用信息
APP_NAME = "职场修仙大护法"
APP_VERSION = "1.0.0"

# 主题模式
THEME_XIANXIA = "xianxia"
THEME_WORKPLACE = "workplace"

# 修仙术语映射
XIANXIA_TERMS = {
    "公司": "宗门", "企业": "仙门", "项目": "秘境试炼", "任务": "悬赏任务",
    "技术": "功法", "技能": "心法", "领导": "掌门", "老板": "长老",
    "同事": "同门", "薪水": "灵石", "预算": "修炼资源", "办公室政治": "心魔",
    "试用期": "外门考核", "转正": "筑基成功", "升职": "突破境界",
    "离职": "另投仙门", "跳槽": "转投仙门", "团队建设": "宗门论道",
    "面试": "入门试炼", "简历": "英雄帖", "加班": "闭关修炼",
    "开会": "论道大会", "汇报": "述职", "KPI": "修炼指标",
    "OKR": "修炼目标", "绩效": "修为考核", "年终奖": "年终灵石分红",
}

# 8大场景定义
SCENES = {
    1: {
        "id": 1,
        "name": "新人入职",
        "xianxia_name": "初入仙门",
        "realm": "炼气期",
        "icon": "🏢",
        "xianxia_icon": "⛩️",
        "description": "刚入职一家新公司，面对全新的环境、流程、人际关系，感到迷茫和焦虑。",
        "inputs_schema": [
            {"key": "company", "type": "text", "required": False, "label": "公司名称/性质", "placeholder": "如：某互联网大厂、创业公司"},
            {"key": "industry", "type": "text", "required": False, "label": "行业", "placeholder": "如：互联网、金融、制造业"},
            {"key": "role", "type": "text", "required": True, "label": "我的岗位", "placeholder": "如：前端开发、产品经理"},
            {"key": "days", "type": "number", "required": True, "label": "入职天数", "placeholder": "如：3", "min_val": 0, "max_val": 365},
            {"key": "confusion", "type": "textarea", "required": True, "label": "我当前的困惑/焦虑", "placeholder": "比如：不知道怎么和同事搭话、对业务完全不熟悉..."},
        ],
        "output_modules": ["公司文化速读卡", "关键人物图谱", "前30天行动清单", "常见踩坑预警清单", "沟通话术模板"],
        "features": ["前30天行动清单", "公司文化速读卡", "关键人物关系图"],
        "data_source": "onboarding",
        "disclaimer": None,
        "example_input": {"company": "某互联网大厂", "industry": "互联网", "role": "前端开发工程师", "days": 5, "confusion": "不知道怎么和同事搭话，对公司的业务和技术栈完全不熟悉，感觉每天都在发呆"},
        "example_questions": [
            "入职一周了，感觉完全融入不了团队，大家都很忙没人理我怎么办？",
            "公司没有新人培训，我该怎么快速了解业务？",
            "第一天上班，该怎么自我介绍才能留下好印象？",
        ],
    },
    2: {
        "id": 2,
        "name": "融入新团队",
        "xianxia_name": "拜入宗门",
        "realm": "筑基期",
        "icon": "👥",
        "xianxia_icon": "🏔️",
        "description": "进入一个已有默契的新团队，需要快速融入集体、建立信任关系。",
        "inputs_schema": [
            {"key": "size", "type": "select", "required": True, "label": "团队规模", "options": ["3人以下", "3-10人", "10-30人", "30人以上"]},
            {"key": "type", "type": "select", "required": True, "label": "团队类型", "options": ["技术研发", "产品设计", "运营市场", "综合管理", "其他"]},
            {"key": "role", "type": "text", "required": True, "label": "我的角色", "placeholder": "如：后端开发、运营专员"},
            {"key": "atmosphere", "type": "textarea", "required": False, "label": "我感觉到的团队氛围", "placeholder": "如：大家都很忙，不太说话..."},
            {"key": "difficulty", "type": "textarea", "required": True, "label": "我遇到的具体融入困难", "placeholder": "如：感觉被排外、找不到融入的切入点..."},
        ],
        "output_modules": ["团队文化与潜规则预判", "人际关系破冰策略", "建立信任的里程碑", "沟通风格适配建议", "边界感与防御提示"],
        "features": ["团队文化类型测试", "破冰行动清单", "信任建立里程碑"],
        "data_source": "team_integration",
        "disclaimer": None,
        "example_input": {"size": "10-30人", "type": "技术研发", "role": "后端开发工程师", "atmosphere": "大家都很忙，开会时我基本插不上话", "difficulty": "感觉团队已经有自己的圈子，我很难融入，午饭都是他们约好的"},
        "example_questions": [
            "团队已经有自己的小圈子了，我作为新人怎么融入？",
            "技术团队里大家都很闷，我该怎么破冰？",
            "感觉被老员工排外，工作分配总是给我最杂的活",
        ],
    },
    3: {
        "id": 3,
        "name": "接受新项目",
        "xianxia_name": "接取秘境任务",
        "realm": "金丹期",
        "icon": "📋",
        "xianxia_icon": "⚔️",
        "description": "作为执行者被分配到一个全新的项目，领域不熟悉、技术栈陌生、deadline紧迫。",
        "inputs_schema": [
            {"key": "project_name", "type": "text", "required": True, "label": "项目名称/类型", "placeholder": "如：客户管理系统重构"},
            {"key": "tech_stack", "type": "textarea", "required": False, "label": "涉及的陌生技术栈/工具", "placeholder": "如：React、Kubernetes、Flink..."},
            {"key": "deadline", "type": "text", "required": True, "label": "Deadline", "placeholder": "如：2周后、下个月底"},
            {"key": "role", "type": "text", "required": True, "label": "我的角色（执行者）", "placeholder": "如：核心开发、测试负责人"},
            {"key": "blocker", "type": "textarea", "required": True, "label": "当前最大的卡点", "placeholder": "如：完全没接触过这个技术栈、需求不清晰..."},
        ],
        "output_modules": ["技术/领域快速学习路径", "Boss战模式：核心难点逐个击破", "任务拆解与优先级矩阵", "风险雷达预警", "每日站会/汇报话术模板"],
        "features": ["Boss战模式", "技术栈学习路径图", "任务拆解看板"],
        "data_source": "new_project",
        "disclaimer": None,
        "example_input": {"project_name": "客户管理系统重构", "tech_stack": "React + TypeScript + GraphQL", "deadline": "3周后", "role": "核心开发", "blocker": "之前一直用Vue，没接触过React，GraphQL也不熟，感觉无从下手"},
        "example_questions": [
            "被分配了一个完全陌生的技术栈项目，两周后要交付，怎么快速上手？",
            "项目需求不清晰，但deadline已经定了，怎么办？",
            "作为新人被安排了核心开发任务，压力大不知道从哪里开始",
        ],
    },
    4: {
        "id": 4,
        "name": "适应新领导",
        "xianxia_name": "新掌门登基",
        "realm": "元婴期",
        "icon": "🎭",
        "xianxia_icon": "👑",
        "description": "换了新领导，管理风格、期望、沟通方式都变了，需要快速适应。",
        "inputs_schema": [
            {"key": "leader_style", "type": "textarea", "required": False, "label": "新领导风格描述", "placeholder": "如：控制欲很强、喜欢看细节、经常临时加需求..."},
            {"key": "mbti", "type": "text", "required": False, "label": "领导/我的MBTI（如有）", "placeholder": "如：ENTJ / ISFP"},
            {"key": "role", "type": "text", "required": True, "label": "我的岗位", "placeholder": "如：高级开发、产品经理"},
            {"key": "issues", "type": "textarea", "required": True, "label": "相处中遇到的问题/摩擦", "placeholder": "如：领导总是改需求、沟通不到点子上..."},
        ],
        "output_modules": ["领导风格画像与期望分析", "工作方式适配方案", "向上管理与沟通策略", "高压线避坑指南", "沟通话术模板"],
        "features": ["MBTI领导风格匹配", "星座趣味解读（仅供娱乐）", "向上管理话术"],
        "data_source": "new_leader",
        "disclaimer": "MBTI和星座分析仅供娱乐参考，不构成专业心理评估或人格诊断。请结合实际情况理性看待分析结果，切勿以此作为人事决策的唯一依据。",
        "example_input": {"leader_style": "控制欲很强，喜欢看代码细节，经常临时加需求，开会喜欢长篇大论", "mbti": "ENTJ", "role": "高级前端开发", "issues": "领导总是改需求，我刚做完他又改了，沟通时他听不进我的意见"},
        "example_questions": [
            "新领导是ENTJ型，控制欲很强，我该怎么和他相处？",
            "领导总是临时加需求，我该怎么拒绝或管理他的预期？",
            "换了领导后感觉之前的工作方式都不对了，怎么快速适应？",
        ],
    },
    5: {
        "id": 5,
        "name": "组织新变革",
        "xianxia_name": "宗门大改",
        "realm": "化神期",
        "icon": "🌪️",
        "xianxia_icon": "🌀",
        "description": "公司或团队进行组织架构调整、流程变革、技术转型等，需要找到自己的位置。",
        "inputs_schema": [
            {"key": "change_type", "type": "select", "required": True, "label": "变革类型", "options": ["组织架构调整", "流程变革", "技术转型", "业务方向调整", "其他"]},
            {"key": "change_scope", "type": "text", "required": False, "label": "涉及范围", "placeholder": "如：整个事业部、仅技术部"},
            {"key": "role", "type": "text", "required": True, "label": "我的岗位", "placeholder": "如：中级开发、运营主管"},
            {"key": "concerns", "type": "textarea", "required": True, "label": "我的担忧与焦虑", "placeholder": "如：担心被裁、不知道新架构下我的定位..."},
        ],
        "output_modules": ["变革影响雷达分析", "个人SWOT分析与定位策略", "技能与心态转型建议", "机会窗口识别清单", "情绪管理与压力释放指南"],
        "features": ["变革影响雷达图", "个人SWOT分析", "转型技能地图"],
        "data_source": "org_change",
        "disclaimer": None,
        "example_input": {"change_type": "组织架构调整", "change_scope": "整个技术部", "role": "中级后端开发", "concerns": "听说要合并团队，不知道我会不会被裁，也不知道新领导是谁"},
        "example_questions": [
            "公司要组织架构调整，听说要裁员，我该怎么准备？",
            "技术栈要从Java转Go，我该怎么规划学习？",
            "部门合并后不知道自己的定位，很焦虑",
        ],
    },
    6: {
        "id": 6,
        "name": "快学新东西",
        "xianxia_name": "修炼新功法",
        "realm": "炼体期",
        "icon": "📚",
        "xianxia_icon": "📖",
        "description": "需要快速学习一项新技能或新知识，时间有限但要求快速上手。",
        "inputs_schema": [
            {"key": "goal", "type": "text", "required": True, "label": "学习目标/新知识", "placeholder": "如：学习Rust语言、掌握数据分析"},
            {"key": "current_level", "type": "select", "required": True, "label": "目前基础", "options": ["零基础", "了解概念", "有类似经验", "有一定基础"]},
            {"key": "time_available", "type": "text", "required": True, "label": "可用时间", "placeholder": "如：每天2小时、周末全天"},
            {"key": "purpose", "type": "select", "required": True, "label": "学习目的", "options": ["工作需要", "转岗准备", "个人兴趣", "面试需要"]},
            {"key": "specific_questions", "type": "textarea", "required": False, "label": "具体疑问", "placeholder": "如：不知道从哪里开始、看文档看不懂..."},
        ],
        "output_modules": ["个性化学习路径规划", "核心知识点脑图梳理", "实战练习/MVP项目建议", "高效学习资源推荐", "学习避坑与瓶颈突破指南"],
        "features": ["AI知识库辅助", "个性化学习路径", "知识点脑图", "实战项目推荐"],
        "data_source": "fast_learning",
        "disclaimer": None,
        "example_input": {"goal": "学习Rust语言", "current_level": "有类似经验", "time_available": "每天2小时", "purpose": "工作需要", "specific_questions": "有C++基础，但Rust的所有权机制看不懂"},
        "example_questions": [
            "零基础想学Python做数据分析，每天只有1小时，怎么规划？",
            "公司要求学Kubernetes，我连Docker都不熟，两周内要上手",
            "学了很多教程但感觉还是不会用，怎么提高学习效率？",
        ],
    },
    7: {
        "id": 7,
        "name": "新带团队",
        "xianxia_name": "开宗立派",
        "realm": "合体期",
        "icon": "🏆",
        "xianxia_icon": "🚩",
        "description": "第一次当团队Leader，从个人贡献者转为管理者，面临全新挑战。",
        "inputs_schema": [
            {"key": "size", "type": "number", "required": True, "label": "团队规模（人数）", "placeholder": "如：5", "min_val": 1, "max_val": 100},
            {"key": "type", "type": "select", "required": True, "label": "团队类型/职能", "options": ["技术研发", "产品设计", "运营市场", "综合管理", "其他"]},
            {"key": "experience", "type": "select", "required": True, "label": "管理经验", "options": ["完全没有", "带过实习生", "做过小组长", "其他"]},
            {"key": "status", "type": "textarea", "required": False, "label": "团队现状描述", "placeholder": "如：团队士气低落、新老交替中..."},
            {"key": "challenge", "type": "textarea", "required": True, "label": "当前面临的最大挑战", "placeholder": "如：不知道怎么分配任务、老员工不服管..."},
        ],
        "output_modules": ["角色转换核心认知", "团队建设路线图", "目标管理与任务分配框架", "1v1深度沟通话术与模板", "新手管理常见陷阱与冲突处理"],
        "features": ["管理风格自测", "团队建设路线图", "1v1沟通话术模板", "目标管理OKR模板"],
        "data_source": "team_leading",
        "disclaimer": None,
        "example_input": {"size": 5, "type": "技术研发", "experience": "完全没有", "status": "团队里有两个老员工，技术很好但不太配合", "challenge": "不知道怎么分配任务，怕分多了老员工有意见，分少了新人做不完"},
        "example_questions": [
            "第一次带5人技术团队，完全没有管理经验，从哪里开始？",
            "老员工不服管，觉得我技术不如他，怎么建立威信？",
            "从技术转管理，感觉自己什么都不会了，怎么适应？",
        ],
    },
    8: {
        "id": 8,
        "name": "新负责项目",
        "xianxia_name": "执掌仙门大阵",
        "realm": "大乘期",
        "icon": "🎯",
        "xianxia_icon": "🏛️",
        "description": "第一次作为项目负责人全权负责一个项目，需要全局视角进行规划和管理。",
        "inputs_schema": [
            {"key": "project_name", "type": "text", "required": True, "label": "项目名称/业务", "placeholder": "如：电商平台年度大促"},
            {"key": "scale", "type": "text", "required": True, "label": "规模与周期", "placeholder": "如：3个月、涉及5个部门"},
            {"key": "headcount", "type": "number", "required": True, "label": "团队人数", "placeholder": "如：15", "min_val": 1, "max_val": 500},
            {"key": "phase", "type": "select", "required": True, "label": "当前所处阶段", "options": ["启动阶段", "规划阶段", "执行阶段", "收尾阶段"]},
            {"key": "budget", "type": "text", "required": False, "label": "预算/资源情况", "placeholder": "如：预算紧张、人力不足"},
            {"key": "challenge", "type": "textarea", "required": True, "label": "作为负责人最大的挑战", "placeholder": "如：跨部门协调困难、需求频繁变更..."},
        ],
        "output_modules": ["项目全局规划框架", "干系人地图与管理策略", "资源分配矩阵与协调话术", "核心风险登记册与预案", "里程碑管理机制"],
        "features": ["一次性完整项目管理报告", "项目规划模板", "资源分配矩阵", "干系人地图"],
        "data_source": "project_managing",
        "disclaimer": None,
        "example_input": {"project_name": "电商平台年度大促活动", "scale": "2个月，涉及技术、产品、运营3个部门", "headcount": 15, "phase": "规划阶段", "budget": "人力紧张，还有其他项目并行", "challenge": "跨部门协调很困难，产品需求频繁变更，技术资源不足"},
        "example_questions": [
            "第一次负责一个15人的项目，不知道怎么规划和分配任务",
            "跨部门项目，其他部门不配合，怎么推动？",
            "项目需求一直在变，怎么控制范围蔓延？",
        ],
    },
}

# localStorage 键名
STORAGE_KEY_CONFIG = "dahuafa_config"
STORAGE_KEY_THEME = "dahuafa_theme"
STORAGE_KEY_HISTORY = "dahuafa_history"

# API调用参数
API_DEFAULT_TIMEOUT = 30
API_MAX_TOKENS = 8192
API_TEMPERATURE = 0.7
API_MAX_RETRIES = 1
API_RETRY_DELAY = 3
API_TEST_TIMEOUT = 10
USER_INPUT_MAX_LENGTH = 2000

# 防刷机制
ANTI_SPAM_INTERVAL = 30  # 秒

# 免责声明
GENERAL_DISCLAIMER = "⚠️ 本内容由AI生成，仅供参考，不构成专业建议。请结合自身实际情况做出判断和决策。"
SCENE4_DISCLAIMER = "🔴 MBTI和星座分析仅供娱乐参考，不构成专业心理评估或人格诊断。请结合实际情况理性看待分析结果，切勿以此作为人事决策的唯一依据。"
