# Angry Judge: The Short Rant Contest

[![make.fun](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/thanhvu261090/makefun-angry-judge-rant/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/thanhvu261090/makefun-angry-judge-rant/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

A short, funny rant about a small everyday annoyance — a printer that only
jams when the deadline is real — written for the
[Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
on make.fun. A furious judge model reads the rants two at a time and picks
the one that lands hardest.

## The entry

> My printer only jams when the deadline is real. Ten blank pages? Flawless. One page, due in five minutes? It swallows the paper whole, blinks an error light I have never seen in my life, and prints a test page in a language I do not speak. I have replaced the ink twice. The ink was never the problem. The problem is a machine that can smell fear — and it is laughing at me in 300 dpi.

**385 characters** (limit: 400), one line.

## How it works

`main.py` (Python 3.13, standard library only) holds the rant as a single
string, checks it against the competition gate — 1 to 400 characters, not
only whitespace, a single line, no leading or trailing whitespace — then
writes it to `/output/entry.txt` and prints it.

```sh
python3 main.py
```
