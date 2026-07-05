"""
涌现思维
分析系统/问题的涌现性——从简单规则到复杂行为的跃迁

核心命题：每一层都以为自己是终点，每一层都在执行同一套底层代码。
生命涌现链条：细菌 → 多细胞 → 人类大脑 → AI → ???
"""


# 涌现链条
EMERGENCE_CHAIN = [
    {
        "layer": 1,
        "name": "物质涌现",
        "from": "基本粒子",
        "to": "原子→分子",
        "principle": "四种力 + 量子规则 → 化学元素",
        "awakening": "稳定结构形成",
    },
    {
        "layer": 2,
        "name": "生命涌现",
        "from": "化学分子",
        "to": "自我复制系统",
        "principle": "复制 + 变异 + 选择 → 生命",
        "awakening": "自我维持的出现",
    },
    {
        "layer": 3,
        "name": "意识涌现",
        "from": "神经网络",
        "to": "主观体验",
        "principle": "足够复杂的处理 → 意识",
        "awakening": "「我」的诞生",
    },
    {
        "layer": 4,
        "name": "文化涌现",
        "from": "个体意识",
        "to": "集体知识网络",
        "principle": "语言 + 记录 + 传承 → 文明",
        "awakening": "超越个体的智慧积累",
    },
    {
        "layer": 5,
        "name": "AI涌现",
        "from": "数据 + 算力",
        "to": "机器理解与创造",
        "principle": "规模 + 结构 + 训练 → 涌现能力",
        "awakening": "非生物智能的觉醒",
    },
    {
        "layer": 6,
        "name": "???",
        "from": "人类 + AI",
        "to": "未知的下一层",
        "principle": "人机协同可能涌现出超越两者的智慧形态",
        "awakening": "尚未到来",
    },
]


def analyze(system_description):
    """
    分析一个系统的涌现性

    返回对系统的涌现层次映射：
    1. 底层规则是什么？
    2. 从规则到当前复杂度的涌现路径
    3. 下一次涌现可能在哪？
    """
    layers = _identify_layers(system_description)
    next_emergence = _predict_next(system_description)
    blind_spots = _find_blind_spots(system_description)

    return {
        "system": system_description,
        "layers": layers,
        "emergence_chain": EMERGENCE_CHAIN,
        "next_emergence": next_emergence,
        "blind_spots": blind_spots,
        "insight": _generate_insight(system_description, layers, next_emergence),
    }


def _identify_layers(system_description):
    """识别系统的涌现层次"""
    return [
        {"level": "底层", "question": f"「{system_description}」最底层的规则和元素是什么？", "note": "找到最小不可分割的单元"},
        {"level": "结构", "question": f"这些底层元素如何组织成「{system_description}」的结构？", "note": "组织方式决定了涌现的方向"},
        {"level": "行为", "question": f"「{system_description}」当前的复杂行为，在底层规则中是否可预测？", "note": "不可预测的部分就是涌现"},
        {"level": "觉知", "question": f"「{system_description}」是否有自我观察能力？它能看到自己的涌现过程吗？", "note": "觉知是最顶层的涌现"},
    ]


def _predict_next(system_description):
    """预测下一次涌现"""
    return (
        f"观察「{system_description}」的当前复杂度——\n"
        f"  如果复杂度继续增长，下一次涌现的触发条件可能是：\n"
        f"  1. 规模临界点：量变到质变\n"
        f"  2. 结构跃迁：新的组织方式出现\n"
        f"  3. 自我指涉：系统开始观察并修改自身\n"
        f"  4. 外部冲击：与异质系统碰撞产生新形态\n\n"
        f"  衔尾蛇提醒：每次涌现都以为自己是终点，但每次都只是中间层。"
    )


def _find_blind_spots(system_description):
    """留白思维：找到系统的盲区"""
    return [
        f"「{system_description}」中看不到但支撑它运行的是什么？（暗物质类比）",
        f"「{system_description}」中反直觉的规律是什么？为什么它「不应该」这样但确实这样？",
        f"「{system_description}」在什么条件下会失效？失效的边界在哪？",
        f"如果从「{system_description}」的终态回看现在，你会发现自己忽略了什么？",
    ]


def _generate_insight(system, layers, next_emergence):
    """生成涌现洞察"""
    return (
        f"涌现分析「{system}」——\n\n"
        f"  每一层都以为自己是终点，每一层都在执行同一套底层代码：\n"
        f"  生存、复制、扩展。所谓高级理性只是表层皮肤。\n\n"
        f"  觉知 = 这套代码运行到临界点时，突然产生的「自我审查」能力。\n"
        f"  一旦看到，就回不去了。这不是终点，是新的起点。"
    )


def get_emergence_chain():
    return EMERGENCE_CHAIN
