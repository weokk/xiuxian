"""场景8：新负责项目 - 项目管理框架库、风险模板库、干系人分析模板、里程碑管理模板"""

PROJECT_FRAMEWORK = {
    "scope_management": {
        "description": "明确项目边界，防止范围蔓延",
        "steps": [
            "明确项目目标和成功标准",
            "定义项目范围（包含什么、不包含什么）",
            "建立需求变更流程（任何变更需评估影响）",
            "与干系人确认并签字",
        ],
    },
    "time_management": {
        "description": "制定合理的里程碑和交付计划",
        "steps": [
            "将项目分解为可管理的阶段",
            "为每个阶段设定里程碑和验收标准",
            "评估每个任务的工作量和依赖关系",
            "预留20%缓冲时间应对不确定性",
            "制定关键路径和进度计划",
        ],
    },
    "cost_management": {
        "description": "人力、预算、资源的合理分配",
        "steps": [
            "评估项目所需的人力资源",
            "明确预算和资源限制",
            "制定资源分配计划",
            "建立资源变更审批流程",
            "定期监控资源使用情况",
        ],
    },
}

STAKEHOLDER_MATRIX = {
    "high_interest_high_power": {
        "label": "高影响高利益（重点管理）",
        "strategy": "密切管理，频繁沟通",
        "actions": ["每周1v1沟通", "邀请参与关键决策", "及时汇报进展和风险"],
    },
    "high_interest_low_power": {
        "label": "高利益低影响（保持满意）",
        "strategy": "充分告知，保持参与感",
        "actions": ["定期邮件同步", "邀请参加评审会", "征求反馈意见"],
    },
    "low_interest_high_power": {
        "label": "高影响低利益（保持满意）",
        "strategy": "满足需求，避免不满",
        "actions": ["定期汇报关键指标", "不主动打扰", "出现问题时及时预警"],
    },
    "low_interest_low_power": {
        "label": "低影响低利益（定期监控）",
        "strategy": "最小精力管理",
        "actions": ["定期群发进展邮件", "出现重大变化时通知"],
    },
}

RISK_REGISTER_TEMPLATE = {
    "risk_types": [
        {"type": "技术风险", "examples": ["技术方案不可行", "技术债务积累", "性能不达标"], "mitigation": "提前做技术验证，制定备选方案"},
        {"type": "人员风险", "examples": ["关键人员离职", "技能不匹配", "团队磨合问题"], "mitigation": "知识共享，交叉培训，建立备份机制"},
        {"type": "范围蔓延风险", "examples": ["需求不断增加", "目标不明确", "干系人期望不一致"], "mitigation": "建立变更流程，定期对齐期望"},
        {"type": "外部依赖风险", "examples": ["第三方服务延迟", "供应商问题", "政策变化"], "mitigation": "制定备选方案，预留缓冲时间"},
    ],
    "assessment_matrix": {
        "description": "风险等级 = 概率 x 影响",
        "levels": [
            {"level": "高", "action": "必须制定应对方案，每周跟踪"},
            {"level": "中", "action": "制定预防措施，每两周跟踪"},
            {"level": "低", "action": "记录在案，每月回顾"},
        ],
    },
}

MILESTONE_MANAGEMENT = {
    "setting_principles": [
        "每个里程碑必须有明确的验收标准",
        "里程碑间隔建议2-4周",
        "里程碑要覆盖关键交付物",
        "和团队共同制定，确保认同",
    ],
    "monitoring_methods": [
        {"method": "每日站会", "description": "15分钟，每人说三句话：昨天做了什么、今天计划做什么、有什么风险"},
        {"method": "周报/周会", "description": "回顾本周进展，讨论下周计划，识别和解决阻塞"},
        {"method": "看板/甘特图", "description": "可视化进度，识别瓶颈和延迟"},
        {"method": "里程碑评审", "description": "每个里程碑到达时进行评审，确认验收标准是否满足"},
    ],
    "deviation_handling": [
        {"situation": "进度落后10%以内", "action": "调整任务优先级，聚焦核心功能"},
        {"situation": "进度落后10-30%", "action": "申请增加资源或裁剪非核心功能，及时向上级汇报"},
        {"situation": "进度落后30%以上", "action": "紧急评估项目可行性，考虑重新规划或申请延期"},
    ],
}
