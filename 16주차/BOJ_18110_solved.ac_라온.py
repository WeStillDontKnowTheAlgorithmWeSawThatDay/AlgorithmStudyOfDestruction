# 파이썬의 round 방식, readline 추가

import sys
input = sys.stdin.readline

n = int(input())
difficulties = [int(input()) for _ in range(n)]
difficulties.sort()
if n == 0:
    print(0)
else:
    people = round(n * 0.15 + 0.0000001)
    sum = 0
    for i in range(people, n-people):
        sum += difficulties[i]
    print(round(sum/(n-2*people) + 0.0000001))
