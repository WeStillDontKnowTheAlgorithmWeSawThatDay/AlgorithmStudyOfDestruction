import sys

from collections import deque


input = sys.stdin.readline
def custom_round(v):
    if v - int(v) >= 0.5:
        return int(v) + 1
    else:
        return int(v)


n = int(input())
ranks = [int(input()) for x in range(n)]
ranks.sort()
ranks = deque(ranks)
cut = custom_round((n * 15) / 100)

for _ in range(cut):
    ranks.popleft()
    ranks.pop()

n -= (cut * 2)


if n <= 0:
    print(0)
else:
    print(custom_round(sum(ranks) / n))
