"""
周易卦象引擎
模拟传统三币占法，生成卦象并提供哲学解读
"""
import json
import random
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "hexagrams.json"

# 八卦
TRIGRAMS = {
    "坤": {"binary": "000", "symbol": "☷", "nature": "地", "attribute": "顺"},
    "艮": {"binary": "001", "symbol": "☶", "nature": "山", "attribute": "止"},
    "坎": {"binary": "010", "symbol": "☵", "nature": "水", "attribute": "陷"},
    "巽": {"binary": "011", "symbol": "☴", "nature": "风", "attribute": "入"},
    "震": {"binary": "100", "symbol": "☳", "nature": "雷", "attribute": "动"},
    "离": {"binary": "101", "symbol": "☲", "nature": "火", "attribute": "丽"},
    "兑": {"binary": "110", "symbol": "☱", "nature": "泽", "attribute": "悦"},
    "乾": {"binary": "111", "symbol": "☰", "nature": "天", "attribute": "健"},
}

# 二进制 -> 卦名
BINARY_TO_TRIGRAM = {v["binary"]: k for k, v in TRIGRAMS.items()}

# 后天八卦查表 (上卦行, 下卦列) -> 卦序
# 行列顺序: 乾 兑 离 震 巽 坎 艮 坤
KING_WEN_TABLE = {
    ("乾", "乾"): 1,  ("兑", "乾"): 43, ("离", "乾"): 14, ("震", "乾"): 34,
    ("巽", "乾"): 9,  ("坎", "乾"): 5,  ("艮", "乾"): 26, ("坤", "乾"): 11,
    ("乾", "兑"): 10, ("兑", "兑"): 58, ("离", "兑"): 38, ("震", "兑"): 54,
    ("巽", "兑"): 61, ("坎", "兑"): 60, ("艮", "兑"): 41, ("坤", "兑"): 19,
    ("乾", "离"): 13, ("兑", "离"): 49, ("离", "离"): 30, ("震", "离"): 55,
    ("巽", "离"): 37, ("坎", "离"): 63, ("艮", "离"): 22, ("坤", "离"): 36,
    ("乾", "震"): 25, ("兑", "震"): 17, ("离", "震"): 21, ("震", "震"): 51,
    ("巽", "震"): 42, ("坎", "震"): 3,  ("艮", "震"): 27, ("坤", "震"): 24,
    ("乾", "巽"): 44, ("兑", "巽"): 28, ("离", "巽"): 50, ("震", "巽"): 32,
    ("巽", "巽"): 57, ("坎", "巽"): 48, ("艮", "巽"): 18, ("坤", "巽"): 46,
    ("乾", "坎"): 6,  ("兑", "坎"): 47, ("离", "坎"): 64, ("震", "坎"): 40,
    ("巽", "坎"): 59, ("坎", "坎"): 29, ("艮", "坎"): 4,  ("坤", "坎"): 7,
    ("乾", "艮"): 33, ("兑", "艮"): 31, ("离", "艮"): 56, ("震", "艮"): 62,
    ("巽", "艮"): 53, ("坎", "艮"): 39, ("艮", "艮"): 52, ("坤", "艮"): 15,
    ("乾", "坤"): 12, ("兑", "坤"): 45, ("离", "坤"): 35, ("震", "坤"): 16,
    ("巽", "坤"): 20, ("坎", "坤"): 8,  ("艮", "坤"): 23, ("坤", "坤"): 2,
}


def load_hexagrams():
    """加载64卦数据"""
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {h["number"]: h for h in data}


def toss_coins():
    """
    模拟三币占法
    正面=3, 反面=2
    三币之和:
      9 = 老阳(变) ⚊→⚋
      8 = 少阴     ⚋
      7 = 少阳     ⚊
      6 = 老阴(变) ⚋→⚊
    返回: (数值, 是否变爻, 爻性)
    """
    coins = [random.choice([2, 3]) for _ in range(3)]
    total = sum(coins)
    if total == 9:
        return (9, True, "yang")   # 老阳
    elif total == 8:
        return (8, False, "yin")   # 少阴
    elif total == 7:
        return (7, False, "yang")  # 少阳
    else:
        return (6, True, "yin")    # 老阴


def divine(question=""):
    """
    完整占卦流程
    返回 dict: {
        question, lines, changing_lines, hexagram, changed_hexagram
    }
    """
    lines = []
    changing = []
    for i in range(6):
        value, is_changing, nature = toss_coins()
        lines.append({
            "position": i + 1,
            "value": value,
            "nature": nature,
            "changing": is_changing,
            "symbol": "⚊" if nature == "yang" else "⚋",
        })
        if is_changing:
            changing.append(i + 1)

    # 构建二进制 (从下到上)
    binary = "".join("1" if l["nature"] == "yang" else "0" for l in lines)

    # 查卦
    lower_trigram = BINARY_TO_TRIGRAM.get(binary[:3], "乾")
    upper_trigram = BINARY_TO_TRIGRAM.get(binary[3:], "乾")
    king_wen_num = KING_WEN_TABLE.get((upper_trigram, lower_trigram), 1)

    hexagrams = load_hexagrams()
    hexagram = hexagrams[king_wen_num]

    # 变卦
    changed_hexagram = None
    if changing:
        changed_binary = list(binary)
        for pos in changing:
            idx = pos - 1
            changed_binary[idx] = "1" if changed_binary[idx] == "0" else "0"
        changed_binary_str = "".join(changed_binary)
        changed_lower = BINARY_TO_TRIGRAM.get(changed_binary_str[:3], "乾")
        changed_upper = BINARY_TO_TRIGRAM.get(changed_binary_str[3:], "乾")
        changed_num = KING_WEN_TABLE.get((changed_upper, changed_lower), 1)
        changed_hexagram = hexagrams[changed_num]

    return {
        "question": question,
        "lines": lines,
        "binary": binary,
        "changing_lines": changing,
        "lower_trigram": lower_trigram,
        "upper_trigram": upper_trigram,
        "hexagram": hexagram,
        "changed_hexagram": changed_hexagram,
    }


def get_hexagram(number):
    """按卦序获取单卦"""
    hexagrams = load_hexagrams()
    return hexagrams.get(number)


def get_all_hexagrams():
    """获取全部64卦"""
    return load_hexagrams()


def format_hexagram_visual(hexagram_data, lines=None):
    """
    格式化卦象可视化
    从下到上显示六爻
    """
    visual = []
    if lines:
        for i in range(5, -1, -1):
            line = lines[i]
            marker = " ○" if line["changing"] else "  "
            visual.append(f"  {line['symbol']}{marker}  (第{line['position']}爻)")
    else:
        binary = hexagram_data["binary"]
        for i in range(5, -1, -1):
            bit = binary[i]
            symbol = "⚊" if bit == "1" else "⚋"
            pos = i + 1
            visual.append(f"  {symbol}    (第{pos}爻)")

    upper = TRIGRAMS.get(hexagram_data["upper"], {})
    lower = TRIGRAMS.get(hexagram_data["lower"], {})

    visual.append("")
    visual.append(f"  上卦: {upper.get('symbol', '?')} {hexagram_data['upper']} ({upper.get('nature', '?')})")
    visual.append(f"  下卦: {lower.get('symbol', '?')} {hexagram_data['lower']} ({lower.get('nature', '?')})")

    return "\n".join(visual)
