"""
衔尾蛇闭环
映射循环和反馈回路，发现系统的自增强/自削弱结构

衔尾蛇 = 蛇咬住自己尾巴 = 终点回到起点 = 螺旋上升的闭环
核心：觉醒/觉知 → 预测 → 时间差 → 价值 → 能量 → 觉知升级 → 更强觉知
"""


# 衔尾蛇闭环模板
OUROBOROS_CYCLES = {
    "觉知闭环": {
        "loop": "觉知 → 预测能力 → 时间差 → 价值创造 → 资源积累 → 觉知升级 → 更强觉知",
        "principle": "每一次循环都在更高的维度闭合。不是回到原点，是螺旋上升。",
        "key": "觉知是引擎，预测是工具，时间差是杠杆。",
    },
    "学习闭环": {
        "loop": "学习 → 实践 → 反馈 → 调整 → 更深理解 → 更好实践 → 更准反馈",
        "principle": "反馈的频率和精度决定闭环的加速度。",
        "key": "闭环不快是因为反馈太慢或太模糊。",
    },
    "创造闭环": {
        "loop": "创造 → 分享 → 反馈 → 迭代 → 更好的创造 → 更广的分享",
        "principle": "创造的价值在流通中增值，在囤积中衰减。",
        "key": "分享是闭环的加速器，也是创造的一部分。",
    },
    "成长闭环": {
        "loop": "挑战 → 尝试 → 失败 → 反思 → 突破 → 更大挑战",
        "principle": "没有失败的闭环是假的。真正的闭环需要负反馈。",
        "key": "失败是闭环中不可缺少的一环，跳过失败就跳过了成长。",
    },
    "关系闭环": {
        "loop": "信任 → 坦诚 → 理解 → 共鸣 → 更深信任",
        "principle": "信任在坦诚中增长，在隐瞒中消耗。闭环方向取决于每次互动。",
        "key": "闭环可以正向增强，也可以反向削弱。方向由最小的互动决定。",
    },
}


def map_cycle(situation):
    """
    映射一个情境的循环和反馈回路

    返回: {
        situation,
        identified_loops: 识别出的闭环,
        feedback_analysis: 反馈分析,
        leverage_points: 杠杆点,
        insight
    }
    """
    identified = _identify_loops(situation)
    feedback = _analyze_feedback(situation)
    leverage = _find_leverage(situation)

    return {
        "situation": situation,
        "identified_loops": identified,
        "feedback_analysis": feedback,
        "leverage_points": leverage,
        "templates": OUROBOROS_CYCLES,
        "insight": _generate_insight(situation, identified, leverage),
    }


def _identify_loops(situation):
    """识别情境中的闭环"""
    return [
        {"loop": f"「{situation}」中的正反馈循环", "question": "什么行为会导致自我增强？增强的方向是好是坏？"},
        {"loop": f"「{situation}」中的负反馈循环", "question": "什么行为会产生自我纠正？纠正是否及时？"},
        {"loop": f"「{situation}」中的延迟反馈", "question": "哪些反馈需要很久才能看到？延迟导致的误判风险是什么？"},
        {"loop": f"「{situation}」中的隐藏循环", "question": "有没有看不见但在运行的循环？比如情绪循环、信念循环？"},
    ]


def _analyze_feedback(situation):
    """分析反馈机制"""
    return {
        "speed": f"「{situation}」的反馈有多快？反馈越快，闭环加速度越大。",
        "clarity": f"「{situation}」的反馈是否清晰？模糊的反馈比没有反馈更危险。",
        "direction": f"「{situation}」的反馈是增强还是纠正？方向决定了系统是走向爆发还是平衡。",
        "completeness": f"「{situation}」的反馈是否完整？只看到正面反馈会导致盲目乐观。",
    }


def _find_leverage(situation):
    """找到系统杠杆点"""
    return [
        {"point": "规则层", "description": f"「{situation}」的底层规则是什么？改变规则比改变行为有效得多。"},
        {"point": "反馈环", "description": f"「{situation}」的哪个反馈环最关键？缩短它的延迟，或增强它的精度。"},
        {"point": "信息流", "description": f"「{situation}」中信息如何流动？改变信息结构可以改变整个系统行为。"},
        {"point": "临界点", "description": f"「{situation}」离涌现的临界点有多远？在临界点附近，微小的改变可能引发巨大的变化。"},
    ]


def _generate_insight(situation, loops, leverage):
    return (
        f"衔尾蛇分析「{situation}」——\n\n"
        f"  蛇咬住自己尾巴时，才看见了完整的圆。\n"
        f"  终点回到起点，不是重复，是螺旋上升。\n\n"
        f"  每一次循环都在更高的维度闭合。\n"
        f"  看到闭环的人，就能找到杠杆——\n"
        f"  在最小的点上用力，撬动整个系统的方向。"
    )


def get_cycle_templates():
    return OUROBOROS_CYCLES
