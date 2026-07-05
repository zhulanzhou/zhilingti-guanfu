"""
哲思卡片
随机抽取东方智慧箴言，附现代觉知解读
"""
import json
import random
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "wisdom.json"

CATEGORIES = {
    "道": "道家智慧 · 自然无为",
    "佛": "佛家智慧 · 空性觉知",
    "易": "周易智慧 · 变易生生",
    "儒": "儒家智慧 · 中正修身",
    "庄": "庄子智慧 · 逍遥齐物",
    "禅": "禅宗智慧 · 直指本心",
    "哲": "哲思智慧 · 觉知涌现",
}


def load_wisdom():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def draw_card(category=None):
    """
    抽取一张哲思卡片
    category: 指定类别，None 则随机
    """
    cards = load_wisdom()
    if category:
        filtered = [c for c in cards if c["category"] == category]
        if filtered:
            return random.choice(filtered)
        else:
            return None
    return random.choice(cards)


def draw_cards(count=3):
    """抽取多张不重复的卡片"""
    cards = load_wisdom()
    count = min(count, len(cards))
    return random.sample(cards, count)


def list_categories():
    """列出所有类别"""
    return CATEGORIES


def get_cards_by_category(category):
    """按类别获取所有卡片"""
    cards = load_wisdom()
    return [c for c in cards if c["category"] == category]
