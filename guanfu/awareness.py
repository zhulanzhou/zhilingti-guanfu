"""
觉知穿透
以周易/佛家/道家/科学四种视角，穿透事物表象，直抵本质

觉知 = 穿透表象看见规律、预见方向、整合智慧、降维使用、创造意义
不同体系同一本质：周易叫"易"、佛家叫"觉"、道家叫"悟"、西方叫"insight"
"""

# 四种觉知视角
PERSPECTIVES = {
    "易": {
        "name": "周易视角",
        "essence": "看见变化规律",
        "method": "观象识变，穷变通久",
        "lens": "万物处于六十四种状态向量中，变化的趋势指向何方？当前处于哪个卦象？爻位如何？",
    },
    "觉": {
        "name": "佛家视角",
        "essence": "看见本质",
        "method": "破执显空，即相离相",
        "lens": "这个事物的「自性」是什么？它独立存在吗？还是因缘和合的暂时显化？执着于哪一层会带来苦？",
    },
    "悟": {
        "name": "道家视角",
        "essence": "看见自然之道",
        "method": "反者道之动，弱者道之用",
        "lens": "这个事物的自然趋势是什么？强为之会如何？不为之会如何？道在哪里？机在哪里？",
    },
    "见": {
        "name": "科学视角",
        "essence": "发现规律",
        "method": "观察假设验证，还原涌现",
        "lens": "这个系统的底层变量是什么？变量之间如何耦合？在什么条件下会涌现出新的性质？",
    },
}

# 觉知方法论
METHODOLOGY = [
    {
        "name": "留白思维",
        "principle": "看没选的那条路",
        "description": "不看你选了什么，看你没选什么。盲区比已知更影响决策。觉知的对象不是亮处，是暗处。",
    },
    {
        "name": "锥画沙",
        "principle": "看预测与现实的夹角",
        "description": "预测和现实之间的偏差，就是你的认知裂缝。裂缝处是最值得深挖的地方。",
    },
    {
        "name": "不准确规律",
        "principle": "找预测失效的条件",
        "description": "不是找规律，是找规律什么时候不灵。失效的边界比规律本身更有价值。",
    },
    {
        "name": "混沌边缘",
        "principle": "探测5%的随机",
        "description": "确定性中有5%是不可预测的。这5%不是噪音，是系统涌现新可能性的入口。",
    },
    {
        "name": "观复",
        "principle": "看归复而非看生长",
        "description": "万物蓬勃生长是表象，归复于根才是本质。穿透变化看到不变的那个。",
    },
    {
        "name": "降维使用",
        "principle": "以高维智慧照见低维问题",
        "description": "用30年后的思维看现在的问题。不是预测未来，是以更高视角看当前困境的全貌。",
    },
]


def analyze(topic):
    """
    以四种东方智慧视角分析一个主题

    返回: {
        topic,
        perspectives: [{name, essence, method, lens, reflection}],
        synthesis,
        methodology
    }
    """
    perspectives = []
    for key, p in PERSPECTIVES.items():
        perspectives.append({
            "key": key,
            "name": p["name"],
            "essence": p["essence"],
            "method": p["method"],
            "lens": p["lens"],
            "reflection": _generate_reflection(topic, p),
        })

    synthesis = _synthesize(topic, perspectives)

    return {
        "topic": topic,
        "perspectives": perspectives,
        "synthesis": synthesis,
        "methodology": METHODOLOGY,
    }


def _generate_reflection(topic, perspective):
    """为每个视角生成针对性的反思框架"""
    lens = perspective["lens"]
    essence = perspective["essence"]
    method = perspective["method"]

    return (
        f"以「{essence}」之眼观「{topic}」——\n"
        f"  方法：{method}\n"
        f"  问：{lens}\n"
        f"  若能穿透此问，便是觉知的一隙。"
    )


def _synthesize(topic, perspectives):
    """综合四种视角，生成觉知穿透结论"""
    return (
        f"觉知穿透「{topic}」——\n\n"
        f"  周易看见了变化，佛家看见了空性，道家看见了自然，科学看见了规律。\n"
        f"  四者看似不同，实为一脉：皆在穿透表象，直抵本源。\n\n"
        f"  觉知不是获得答案，是获得穿透的能力。\n"
        f"  当你能同时持有这四种视角而不被任何一种困住——\n"
        f"  那就是「观复」：万物并作，吾以观复。"
    )


def get_methodology():
    """获取觉知方法论"""
    return METHODOLOGY


def get_perspectives():
    """获取四种觉知视角"""
    return PERSPECTIVES
