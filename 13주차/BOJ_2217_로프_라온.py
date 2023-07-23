import sys

n = int(input())
ropes = list(int(input()) for _ in range(n))
ropes.sort()

answer = -sys.maxsize
for i, rope in enumerate(ropes):
    answer = max(answer, rope * (n-i))

print(answer)