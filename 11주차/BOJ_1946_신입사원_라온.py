# *, 알고리즘 생각해보기

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(n)]
    scores.sort(key=lambda score:score[0])
    min_score = 100000
    num = 0
    for score1, score2 in scores:
        if score2 <= min_score:
            min_score = score2
            num += 1
    print(num)
