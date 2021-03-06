# 单败双败模拟器

本repo直接目标是能够仿真模拟LPL淘汰赛中从四强开始的单双败赛制。

数值结论是单败与双败不会影响每一个队伍成为某一个名次的概率，更不会影响不同队伍拿到冠军的概率。

仿真规则假设:
- 每个队伍有一个战斗力分数，分数越高，越有可能在一场BO1中获取胜利。两个队伍在一场BO1中对战时，获胜概率取决于两者战斗力分数的比值.
- 选边权特性，在两个队伍打BO1对战时，拥有选边权的一方战斗力得到增强。在BO5番战中，第一局的选边权由赛制决定，后面小局的选边权交给前一小局的败者。

值得注意的假设问题:
- 这里不考虑所谓队伍风格克制问题，也就是强的队伍打所有队伍都一样强，不会因为风格克制问题影响胜负概率。若想增加这一项，可以在match.py中修改 _get_points函数.
- 现实BO5番战中局间胜负关系存在一定的相关性，这里不考虑这一相关性。
- 现实淘汰赛中队伍的战力会持续浮动，这个浮动与比赛进程可能存在一定的相关性，这里不考虑这一相关性。
- 不同队伍拿到选边权之后的增幅系数是不同的，这里暂时忽略了这个问题。

数值结论:
- 单败与双败"几乎"不会影响每一个队伍成为某一个名次的概率，更不会影响不同队伍拿到冠军的概率，与优先选边权无关系。

对实际问题的提供的参考:
- 双败只是增加了比赛场次，从概率来说相对于单败几乎没有变化。
- 双败赛制中，无论是否给予胜者组胜者总决赛场的优先选边权，赛制本身都是足够公平的。优先选边权以及选边优势的存在，队伍战斗力的浮动的相对影响被减小，进一步激励队伍在胜者组决赛中争夺胜利，而不是故意掉入败者组。
- 如果选边增幅系数太大，会使得比赛更看重出身而不是战斗力。这不是好事，但是实际上这个增幅幅度只与游戏版本以及队伍风格有关，与赛制没关系。

## 运行代码

对固定的组合进行模拟，运行
```bash
python3 simulator.py
```

随机队伍的战斗力构成以及优先选边权带来的增幅比例, 并计算单败与双败的概率分布距离(KL-divergence)的均值:
```bash
python3 random_simulator.py
```
