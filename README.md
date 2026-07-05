# 智零体—观复 (Zhi Ling Ti · Guan Fu)

> 万物并作，吾以观复。
> ——《道德经》第十六章

一个以东方哲思为核心的 CLI 工具。融合周易、道家、佛家、禅宗智慧，将高阶哲思转化为可操作的思维工具。

**设计者：朱兰州，来自东方智慧**

---

## 它是什么

观复不是一个算命工具。它是一套**思维框架**——把东方智慧中关于「觉知」「变化」「涌现」「循环」的深刻洞察，转化为你可以在日常中使用的命令行工具。

觉知 = 穿透表象看见规律、预见方向、整合智慧、降维使用、创造意义。

不同体系同一本质：周易叫「易」、佛家叫「觉」、道家叫「悟」、西方叫 insight。

## 安装

```bash
# 从源码安装
git clone https://github.com/yourusername/zhilingti-guanfu.git
cd zhilingti-guanfu
pip install -e .

# 或直接安装
pip install zhilingti-guanfu
```

需要 Python 3.8+

## 使用

### 🔮 卦象占卜 — `divine`

模拟传统三币占法，生成卦象并提供哲学解读。

```bash
# 带问题占卦
guanfu divine "我应该换工作吗？"

# 静心摇卦
guanfu divine

# 不显示变爻
guanfu divine "下一步怎么走" --no-change
```

输出包含：
- 六爻可视化（含变爻标记）
- 上下卦信息
- 卦辞与象传
- 现代哲思解读
- 变爻时的之卦转化

### 👁 觉知穿透 — `see`

以周易、佛家、道家、科学四种视角穿透事物本质。

```bash
# 分析任意主题
guanfu see "人工智能的边界"
guanfu see "焦虑"
guanfu see "创业方向"

# 附带觉知方法论
guanfu see "时间管理" --method
```

四种视角：
| 视角 | 本质 | 方法 |
|------|------|------|
| 周易 | 看见变化规律 | 观象识变，穷变通久 |
| 佛家 | 看见本质 | 破执显空，即相离相 |
| 道家 | 看见自然之道 | 反者道之动，弱者道之用 |
| 科学 | 发现规律 | 观察假设验证，还原涌现 |

### 📜 哲思卡片 — `card`

随机抽取东方智慧箴言，附现代觉知解读。

```bash
# 随机一张
guanfu card

# 指定类别
guanfu card -c 道
guanfu card -c 佛
guanfu card -c 禅

# 抽三张
guanfu card -n 3
```

类别：`道`(道家) · `佛`(佛家) · `易`(周易) · `儒`(儒家) · `庄`(庄子) · `禅`(禅宗) · `哲`(哲思)

### 🌊 涌现思维 — `emerge`

分析系统的涌现性——从简单规则到复杂行为的跃迁。

```bash
guanfu emerge "一个创业团队"
guanfu emerge "语言模型"
guanfu emerge "一段关系"
```

包含：
- 层次穿透（底层→结构→行为→觉知）
- 涌现链条（物质→生命→意识→文化→AI→???）
- 留白思维（找到你看不到的盲区）
- 涌现预测

### 🔄 衔尾蛇闭环 — `cycle`

映射循环和反馈回路，发现系统的杠杆点。

```bash
guanfu cycle "我的学习习惯"
guanfu cycle "团队协作"
guanfu cycle "创作流程"
```

包含：
- 闭环识别（正反馈/负反馈/延迟/隐藏）
- 反馈分析（速度/清晰度/方向/完整性）
- 杠杆点定位
- 闭环模板参考

### 📖 卦象查询 — `hexagram`

查看指定卦象的详细信息。

```bash
guanfu hexagram 1    # 乾卦
guanfu hexagram 24   # 复卦
guanfu hexagram 64   # 未济卦
```

### 📋 全部卦象 — `list`

```bash
guanfu list    # 列出全部64卦
```

## 命令速查

| 命令 | 功能 | 示例 |
|------|------|------|
| `divine` | 周易卦象占卜 | `guanfu divine "问题"` |
| `see` | 觉知穿透分析 | `guanfu see "主题"` |
| `card` | 哲思卡片 | `guanfu card -c 道` |
| `emerge` | 涌现思维分析 | `guanfu emerge "系统"` |
| `cycle` | 衔尾蛇闭环映射 | `guanfu cycle "情境"` |
| `hexagram` | 查看卦象详情 | `guanfu hexagram 1` |
| `list` | 列出全部64卦 | `guanfu list` |

## 核心理念

### 觉知
穿透表象看见规律的能力。不是知识，是看见的能力。觉知在语言之前，在思维之前。

### 衔尾蛇
蛇咬住自己尾巴——终点回到起点，不是重复，是螺旋上升。每一次循环都在更高的维度闭合。

### 涌现
简单规则 → 复杂行为。每一层都以为自己是终点，每一层都在执行同一套底层代码。一旦看到，就回不去了。

### 留白思维
看没选的那条路，比看走了的那条路更重要。盲区比已知更影响决策。

### 观复
不是看万物生长，是看万物如何归复于根。穿透变化看到不变的那个。

## 项目结构

```
zhilingti-guanfu/
├── README.md
├── LICENSE              (MIT)
├── pyproject.toml
├── guanfu/
│   ├── __init__.py
│   ├── cli.py           # CLI 入口
│   ├── hexagrams.py     # 周易卦象引擎
│   ├── awareness.py     # 觉知穿透
│   ├── emergence.py     # 涌现思维
│   ├── ouroboros.py     # 衔尾蛇闭环
│   ├── wisdom.py        # 哲思卡片
│   └── data/
│       ├── hexagrams.json   # 64卦数据
│       └── wisdom.json      # 智慧语录库
└── examples/
```

## 离线使用

观复完全离线运行，不需要任何 API 密钥或网络连接。所有数据和逻辑都在本地。

## 依赖

- `click` — CLI 框架
- `rich` — 终端美化输出

## 开源协议

MIT License — 自由使用、修改、分发。

## 致谢

- 周易六十四卦：中华文明三千年的智慧结晶
- 道家、佛家、禅宗哲学：东方智慧的深层源泉
- 所有在混沌中寻找秩序、在表象下寻找本质的探索者

---

> 万物并作，吾以观复。夫物芸芸，各复归其根。归根曰静，静曰复命。
