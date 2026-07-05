# 使用示例

## 1. 卦象占卜

```bash
# 带问题占卦
$ guanfu divine "我应该创业吗？"

# 静心摇卦
$ guanfu divine

# 不显示变爻
$ guanfu divine "下一步怎么走" --no-change
```

## 2. 觉知穿透

```bash
# 分析任意主题
$ guanfu see "人工智能的边界"
$ guanfu see "焦虑"
$ guanfu see "时间管理"

# 附带觉知方法论
$ guanfu see "创造力" --method
```

## 3. 哲思卡片

```bash
# 随机一张
$ guanfu card

# 指定类别
$ guanfu card -c 道
$ guanfu card -c 佛
$ guanfu card -c 禅

# 抽三张
$ guanfu card -n 3
```

## 4. 涌现思维

```bash
$ guanfu emerge "一个创业团队"
$ guanfu emerge "语言模型"
$ guanfu emerge "一段关系"
```

## 5. 衔尾蛇闭环

```bash
$ guanfu cycle "我的学习习惯"
$ guanfu cycle "团队协作"
$ guanfu cycle "创作流程"
```

## 6. 卦象查询

```bash
$ guanfu hexagram 1     # 乾卦
$ guanfu hexagram 24    # 复卦
$ guanfu hexagram 64    # 未济卦
```

## 7. 列出全部64卦

```bash
$ guanfu list
```

## 在 Python 代码中使用

```python
from guanfu import hexagrams, wisdom, awareness, emergence, ouroboros

# 卦象占卜
result = hexagrams.divine("我的问题")
print(result["hexagram"]["name"])

# 哲思卡片
card = wisdom.draw_card(category="道")
print(card["text"])

# 觉知穿透
analysis = awareness.analyze("焦虑")
for p in analysis["perspectives"]:
    print(p["name"], p["essence"])

# 涌现分析
em = emergence.analyze("一个团队")
print(em["insight"])

# 衔尾蛇闭环
cycle = ouroboros.map_cycle("学习习惯")
for loop in cycle["identified_loops"]:
    print(loop["loop"])
```
