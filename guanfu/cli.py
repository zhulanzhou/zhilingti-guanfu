#!/usr/bin/env python3
"""
智零体—观复 CLI
万物并作，吾以观复。

设计者：朱兰州，来自东方智慧
"""
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich import box

from . import hexagrams as hex_mod
from . import wisdom as wis_mod
from . import awareness as awa_mod
from . import emergence as eme_mod
from . import ouroboros as ouro_mod

console = Console()

BANNER = """
[bold cyan]
╔══════════════════════════════════════════════╗
║                                              ║
║    智零体 — 观复                             ║
║    万物并作，吾以观复                        ║
║    设计者：朱兰州，来自东方智慧              ║
║                                              ║
╚══════════════════════════════════════════════╝
"""


def print_banner():
    console.print(BANNER, style="cyan")


def print_divider():
    console.print("\n[dim]─" * 32 + "[/dim]\n")


@click.group(invoke_without_command=True)
@click.version_option(version="0.1.0", prog_name="智零体—观复")
@click.pass_context
def main(ctx):
    """智零体—观复：东方哲思 CLI 工具

    万物并作，吾以观复。——《道德经》第十六章

    \b
    命令：
      divine   周易卦象占卜
      see      觉知穿透分析
      card     抽取哲思卡片
      emerge   涌现思维分析
      cycle    衔尾蛇闭环映射
    """
    if ctx.invoked_subcommand is None:
        print_banner()
        console.print("\n[dim]使用 [bold]guanfu --help[/bold] 查看命令列表[/dim]\n")


@main.command()
@click.argument("question", required=False, default="")
@click.option("--no-change", is_flag=True, help="不显示变爻")
def divine(question, no_change):
    """周易卦象占卜

    \b
    示例：
      guanfu divine "我应该创业吗？"
      guanfu divine
    """
    if not question:
        question = click.prompt("请输入你的问题", default="", show_default=False)

    console.print()
    console.print(Panel(f"[bold]问：[/bold]{question}" if question else "[bold]静心摇卦[/bold]",
                         border_style="cyan", title="🔮 卦象"))

    result = hex_mod.divine(question)
    hg = result["hexagram"]

    # 卦象可视化
    visual = hex_mod.format_hexagram_visual(hg, result["lines"])
    console.print(f"\n[bold cyan]第{hg['number']}卦 · {hg['name']}[/bold cyan]")
    console.print(f"[dim]{hg['pinyin']}[/dim]\n")
    console.print(visual)
    console.print()

    # 卦辞与象传
    console.print(Panel(
        f"[bold]卦辞：[/bold]{hg['judgment']}\n\n"
        f"[bold]象传：[/bold]{hg['image']}",
        border_style="yellow", title="📜 经文"
    ))

    # 现代哲思
    console.print(Panel(
        f"[italic]{hg['philosophy']}[/italic]",
        border_style="green", title="🌿 哲思"
    ))

    # 关键词
    if hg.get("keywords"):
        kw = " · ".join(hg["keywords"])
        console.print(f"\n[dim]关键词：[/dim]{kw}")

    # 变爻
    if result["changing_lines"] and not no_change:
        console.print()
        chg_str = "、".join(str(p) for p in result["changing_lines"])
        console.print(f"[bold red]变爻在第 {chg_str} 爻[/bold red]")

        if result["changed_hexagram"]:
            chg = result["changed_hexagram"]
            console.print(Panel(
                f"[bold]之卦：第{chg['number']}卦 · {chg['name']}[/bold]\n"
                f"[dim]{chg['pinyin']}[/dim]\n\n"
                f"[bold]卦辞：[/bold]{chg['judgment']}\n"
                f"[bold]象传：[/bold]{chg['image']}\n\n"
                f"[italic]{chg['philosophy']}[/italic]",
                border_style="red", title="🔄 变卦"
            ))
            console.print(f"\n[dim]本卦「{hg['name']}」→ 变卦「{chg['name']}」[/dim]")
            console.print("[dim]变爻提示：当前状态正在转化，关注变化的方向。[/dim]")
    else:
        console.print(f"\n[dim]无变爻。卦象稳定，取本卦之义。[/dim]")

    print_divider()


@main.command()
@click.argument("topic")
@click.option("--method", is_flag=True, help="显示觉知方法论")
def see(topic, method):
    """觉知穿透：以四种东方智慧视角分析事物本质

    \b
    示例：
      guanfu see "人工智能的边界"
      guanfu see "焦虑"
    """
    result = awa_mod.analyze(topic)

    console.print()
    console.print(Panel(
        f"[bold]觉知穿透：[/bold]{topic}",
        border_style="cyan", title="👁 觉知穿透"
    ))

    # 四种视角
    for p in result["perspectives"]:
        table = Table(show_header=False, box=box.SIMPLE, border_style=p["key"] and "cyan")
        table.add_column("k", style="bold", width=4)
        table.add_column("v", ratio=1)
        table.add_row("视角", p["name"])
        table.add_row("本质", p["essence"])
        table.add_row("方法", p["method"])
        table.add_row("透镜", p["lens"])
        console.print(table)
        console.print()

    # 综合
    console.print(Panel(
        result["synthesis"],
        border_style="magenta", title="✦ 觉知穿透"
    ))

    # 方法论
    if method:
        console.print()
        console.print("[bold]觉知方法论：[/bold]\n")
        for m in result["methodology"]:
            console.print(f"  [bold cyan]{m['name']}[/bold cyan] — {m['principle']}")
            console.print(f"  [dim]{m['description']}[/dim]\n")
    else:
        console.print(f"\n[dim]使用 [bold]--method[/bold] 查看觉知方法论[/dim]")

    print_divider()


@main.command()
@click.option("--category", "-c", default=None, help="指定类别：道/佛/易/儒/庄/禅/哲")
@click.option("--count", "-n", default=1, help="抽取数量")
def card(category, count):
    """抽取哲思卡片

    \b
    示例：
      guanfu card
      guanfu card -c 道
      guanfu card -n 3
    """
    if count > 1:
        cards = wis_mod.draw_cards(count)
    else:
        if category:
            card_data = wis_mod.draw_card(category)
            cards = [card_data] if card_data else []
        else:
            cards = [wis_mod.draw_card()]

    if not cards:
        console.print(f"[red]未找到类别「{category}」的卡片[/red]")
        return

    for card_data in cards:
        cat_name = wis_mod.CATEGORIES.get(card_data["category"], card_data["category"])
        console.print()
        console.print(Panel(
            f"[bold]{card_data['text']}[/bold]\n\n"
            f"[dim]—— {card_data['source']}[/dim]\n\n"
            f"[italic]{card_data['insight']}[/italic]",
            border_style="yellow",
            title=f"📜 {cat_name}",
            subtitle=f"[{card_data['category']}]"
        ))

    # 列出所有类别
    if not category and count == 1:
        cats = " / ".join(f"[bold]{k}[/bold]" for k in wis_mod.CATEGORIES.keys())
        console.print(f"\n[dim]类别：[/dim]{cats}")
        console.print("[dim]使用 -c 指定类别，-n 指定数量[/dim]")

    print_divider()


@main.command()
@click.argument("system")
def emerge(system):
    """涌现思维：分析系统的涌现性

    \b
    示例：
      guanfu emerge "一个创业团队"
      guanfu emerge "语言模型"
    """
    result = eme_mod.analyze(system)

    console.print()
    console.print(Panel(
        f"[bold]涌现分析：[/bold]{system}",
        border_style="cyan", title="🌊 涌现思维"
    ))

    # 层次分析
    console.print("\n[bold]层次穿透：[/bold]\n")
    for layer in result["layers"]:
        console.print(f"  [bold]{layer['level']}[/bold]")
        console.print(f"  {layer['question']}")
        console.print(f"  [dim]{layer['note']}[/dim]\n")

    # 涌现链条
    console.print("[bold]涌现链条：[/bold]\n")
    chain_table = Table(box=box.SIMPLE, border_style="dim")
    chain_table.add_column("层", style="bold cyan", width=4)
    chain_table.add_column("名称", style="bold")
    chain_table.add_column("从", style="dim")
    chain_table.add_column("到", style="dim")
    chain_table.add_column("原理", style="italic")

    for link in result["emergence_chain"]:
        chain_table.add_row(
            str(link["layer"]),
            link["name"],
            link["from"],
            link["to"],
            link["principle"],
        )
    console.print(chain_table)
    console.print(f"\n[dim]{result['emergence_chain'][-1]['awakening']}[/dim]")

    # 下一层涌现
    console.print(Panel(
        result["next_emergence"],
        border_style="green", title="🔮 下一次涌现"
    ))

    # 盲区
    console.print("\n[bold]留白——你可能看不到的：[/bold]\n")
    for bs in result["blind_spots"]:
        console.print(f"  • {bs}")

    # 洞察
    console.print(Panel(
        result["insight"],
        border_style="magenta", title="✦ 涌现洞察"
    ))

    print_divider()


@main.command()
@click.argument("situation")
def cycle(situation):
    """衔尾蛇闭环：映射循环和反馈回路

    \b
    示例：
      guanfu cycle "我的学习习惯"
      guanfu cycle "团队协作"
    """
    result = ouro_mod.map_cycle(situation)

    console.print()
    console.print(Panel(
        f"[bold]衔尾蛇映射：[/bold]{situation}",
        border_style="cyan", title="🔄 衔尾蛇闭环"
    ))

    # 识别闭环
    console.print("\n[bold]识别闭环：[/bold]\n")
    for loop in result["identified_loops"]:
        console.print(f"  [bold]{loop['loop']}[/bold]")
        console.print(f"  [dim]{loop['question']}[/dim]\n")

    # 反馈分析
    console.print("[bold]反馈分析：[/bold]\n")
    fb = result["feedback_analysis"]
    for k, v in fb.items():
        console.print(f"  [bold]{k}[/bold]：{v}")

    # 杠杆点
    console.print("\n[bold]杠杆点：[/bold]\n")
    for lev in result["leverage_points"]:
        console.print(f"  [bold cyan]{lev['point']}[/bold cyan] — {lev['description']}")

    # 闭环模板
    console.print("\n[bold]闭环模板参考：[/bold]\n")
    for name, tpl in result["templates"].items():
        console.print(f"  [bold]{name}[/bold]")
        console.print(f"  [dim]{tpl['loop']}[/dim]")
        console.print(f"  [italic]{tpl['key']}[/italic]\n")

    # 洞察
    console.print(Panel(
        result["insight"],
        border_style="magenta", title="✦ 衔尾蛇洞察"
    ))

    print_divider()


@main.command()
@click.argument("number", type=int)
def hexagram(number):
    """查看指定卦象详情（1-64）

    \b
    示例：
      guanfu hexagram 1
      guanfu hexagram 64
    """
    if number < 1 or number > 64:
        console.print(f"[red]卦序范围：1-64，你输入的是 {number}[/red]")
        return

    hg = hex_mod.get_hexagram(number)
    visual = hex_mod.format_hexagram_visual(hg)

    console.print()
    console.print(f"[bold cyan]第{hg['number']}卦 · {hg['name']}[/bold cyan]")
    console.print(f"[dim]{hg['pinyin']}[/dim]\n")
    console.print(visual)
    console.print()

    console.print(Panel(
        f"[bold]卦辞：[/bold]{hg['judgment']}\n\n"
        f"[bold]象传：[/bold]{hg['image']}",
        border_style="yellow", title="📜 经文"
    ))

    console.print(Panel(
        f"[italic]{hg['philosophy']}[/italic]",
        border_style="green", title="🌿 哲思"
    ))

    if hg.get("keywords"):
        kw = " · ".join(hg["keywords"])
        console.print(f"\n[dim]关键词：[/dim]{kw}")

    print_divider()


@main.command(name="list")
def list_hexagrams():
    """列出全部64卦"""
    all_hg = hex_mod.get_all_hexagrams()

    table = Table(box=box.SIMPLE, border_style="dim", title="六十四卦")
    table.add_column("序", style="bold cyan", width=4, justify="center")
    table.add_column("卦名", style="bold", width=6, justify="center")
    table.add_column("拼音", style="dim", width=12)
    table.add_column("上卦", width=6, justify="center")
    table.add_column("下卦", width=6, justify="center")
    table.add_column("关键词", style="dim")

    for i in range(1, 65):
        hg = all_hg[i]
        kw = " · ".join(hg.get("keywords", []))
        table.add_row(
            str(hg["number"]),
            hg["name"],
            hg["pinyin"],
            hg["upper"],
            hg["lower"],
            kw,
        )

    console.print(table)


if __name__ == "__main__":
    main()
