<div align="center">

# 智零体—观复

**Zhilingti · Guanfu — A command-line tool for thinking, powered by Eastern wisdom.**

*万物并作，吾以观复。* ——《道德经》第十六章

</div>

---

## 中文简介

智零体—观复

**以东方智慧为内核的命令行思维工具。**

不联网，不依赖，不喧哗。

七枚指令，横跨千年——
从三币占卦的随机启悟，到六层涌现的系统性推演；
从四维觉知穿透迷雾，到衔尾蛇闭环让行动自我进化。

它是工具，也是修行。
敲一行命令，得一刻清明。

---

## English Introduction

**A command-line tool for thinking, powered by Eastern wisdom.**

No network. No dependencies. No noise.

Seven commands, spanning millennia —
from coin-cast divination's spark of insight, to six-layer emergence for systemic reasoning;
from four-lens awareness cutting through fog, to the Ouroboros loop where action evolves itself.

It is a tool. It is also a practice.
Type one command. Find a moment of clarity.

---

**设计者：朱兰州，来自东方智慧**
**Designed by Zhu Lanzhou, from Eastern Wisdom**

---

## 它是什么 / What It Is

观复不是一个算命工具。它是一套**思维框架**——把东方智慧中关于「觉知」「变化」「涌现」「循环」的深刻洞察，转化为你可以在日常中使用的命令行工具。

Guanfu is not a fortune-telling tool. It is a **thinking framework** — translating Eastern wisdom on awareness, change, emergence, and cycles into a command-line tool you can use every day.

觉知 = 穿透表象看见规律、预见方向、整合智慧、降维使用、创造意义。不同体系同一本质：周易叫「易」、佛家叫「觉」、道家叫「悟」、西方叫 insight。

## 安装 / Installation

```bash
# 从源码安装 / Install from source
git clone https://github.com/zhulanzhou/zhilingti-guanfu.git
cd zhilingti-guanfu
pip install -e .

# 或直接安装 / Or install directly
pip install zhilingti-guanfu
```

需要 Python 3.8+ / Requires Python 3.8+

## 使用 / Usage

### 🔮 卦象占卜 — `divine`

模拟传统三币占法，生成卦象并提供哲学解读。

```bash
guanfu divine "我应该换工作吗？"
guanfu divine
guanfu divine "下一步怎么走" --no-change
```

### 👁 觉知穿透 — `see`

以周易、佛家、道家、科学四种视角穿透事物本质。

```bash
guanfu see "人工智能的边界"
guanfu see "焦虑"
guanfu see "时间管理" --method
```

### 📜 哲思卡片 — `card`

随机抽取东方智慧箴言，附现代觉知解读。

```bash
guanfu card
guanfu card -c 道
guanfu card -n 3
```

### 🌊 涌现思维 — `emerge`

分析系统的涌现性——从简单规则到复杂行为的跃迁。

```bash
guanfu emerge "一个创业团队"
guanfu emerge "语言模型"
```

### 🔄 衔尾蛇闭环 — `cycle`

映射循环和反馈回路，发现系统的杠杆点。

```bash
guanfu cycle "我的学习习惯"
guanfu cycle "团队协作"
```

### 📖 卦象查询 — `hexagram`

```bash
guanfu hexagram 1    # 乾卦
guanfu hexagram 64   # 未济卦
```

### 📋 全部卦象 — `list`

```bash
guanfu list
```

## 命令速查 / Command Reference

| 命令 | 功能 | 示例 |
|------|------|------|
| `divine` | 卦象占卜 | `guanfu divine "问题"` |
| `see` | 觉知穿透分析 | `guanfu see "主题"` |
| `card` | 哲思卡片 | `guanfu card -c 道` |
| `emerge` | 涌现思维分析 | `guanfu emerge "系统"` |
| `cycle` | 衔尾蛇闭环映射 | `guanfu cycle "情境"` |
| `hexagram` | 查看卦象详情 | `guanfu hexagram 1` |
| `list` | 列出全部64卦 | `guanfu list` |

## 核心理念 / Core Philosophy

**觉知 Awareness** — 穿透表象看见规律的能力。不是知识，是看见的能力。

**衔尾蛇 Ouroboros** — 蛇咬住自己尾巴。终点回到起点，不是重复，是螺旋上升。

**涌现 Emergence** — 简单规则 → 复杂行为。每一层都以为自己是终点，每一层都在执行同一套底层代码。

**留白 Blank Space** — 看没选的那条路，比看走了的那条路更重要。盲区比已知更影响决策。

**观复 Returning** — 不是看万物生长，是看万物如何归复于根。穿透变化看到不变的那个。

## 离线使用 / Offline

观复完全离线运行，不需要任何 API 密钥或网络连接。

Fully offline. No API keys. No network required.

## 依赖 / Dependencies

- `click` — CLI 框架
- `rich` — 终端美化输出

## 开源协议 / License

MIT License — 自由使用、修改、分发。

## 致谢 / Acknowledgments

- 周易六十四卦：中华文明三千年的智慧结晶
- 道家、佛家、禅宗哲学：东方智慧的深层源泉
- 所有在混沌中寻找秩序、在表象下寻找本质的探索者

---

> 万物并作，吾以观复。夫物芸芸，各复归其根。归根曰静，静曰复命。
