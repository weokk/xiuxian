"""场景3：接受新项目 - 任务拆解方法论、风险清单、汇报话术"""

TASK_DECOMPOSITION_METHODS = {
    "four_quadrants": {
        "name": "四象限法（紧急-重要矩阵）",
        "description": "将任务按紧急程度和重要程度分为四个象限",
        "quadrants": [
            {"name": "紧急且重要", "action": "立即做", "examples": ["核心功能开发", "Deadline临近的任务"]},
            {"name": "重要不紧急", "action": "计划做", "examples": ["技术方案设计", "代码重构", "文档编写"]},
            {"name": "紧急不重要", "action": "委托/快速做", "examples": ["简单的bug修复", "会议回复", "邮件处理"]},
            {"name": "不紧急不重要", "action": "延后/不做", "examples": ["非必要的优化", "低优先级的调研"]},
        ],
    },
    "wbs": {
        "name": "WBS工作分解结构",
        "description": "将项目逐层分解为可管理的工作包",
        "steps": ["确定项目主要交付物", "分解为子交付物", "继续分解直到可估算", "为每个工作包估算工时"],
    },
}

PROJECT_RISKS = [
    {"risk": "需求变更频繁", "probability": "高", "impact": "高", "prevention": "建立需求变更流程，每次变更需评估影响", "response": "预留20%缓冲时间，优先保证核心功能"},
    {"risk": "技术方案不可行", "probability": "中", "impact": "高", "prevention": "提前做技术验证（Spike），不盲目开干", "response": "准备备选技术方案，及时向领导汇报风险"},
    {"risk": "依赖方延迟", "probability": "高", "impact": "中", "prevention": "尽早确认依赖关系，建立沟通机制", "response": "制定并行任务计划，减少等待时间"},
    {"risk": "人力不足", "probability": "中", "impact": "高", "prevention": "提前评估工作量，及时申请资源", "response": "裁剪非核心功能，优先交付MVP"},
    {"risk": "估算偏差", "probability": "高", "impact": "中", "prevention": "参考历史数据，留出缓冲", "response": "及时同步进度偏差，调整计划"},
]

DAILY_STANDUP_SCRIPTS = {
    "template": "昨天：{yesterday_done}\n今天：{today_plan}\n风险：{risks}",
    "examples": [
        "昨天完成了用户登录模块的开发和自测。今天计划开始做订单列表页面。风险：接口文档还没出，可能影响进度。",
        "昨天在排查一个数据同步的bug，已经定位到原因。今天会修复并部署测试。没有特别的风险。",
    ],
    "weekly_report": "## 本周工作总结\n\n### 完成事项\n- {done_items}\n\n### 进行中\n- {in_progress}\n\n### 下周计划\n- {next_week_plan}\n\n### 风险与求助\n- {risks_and_help}",
}
