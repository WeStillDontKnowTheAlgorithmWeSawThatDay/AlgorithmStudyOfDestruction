import sys

input = sys.stdin.readline

ropes = sorted([int(input()) for _ in range(int(input()))], reverse=True)

max_weight = max(rope * (i+1) for i, rope in enumerate(ropes))
print(max_weight)
