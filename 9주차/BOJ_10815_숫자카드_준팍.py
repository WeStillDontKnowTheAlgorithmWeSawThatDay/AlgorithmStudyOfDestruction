import sys

input = sys.stdin.readline

N = int(input())
myCards = set(map(int, input().split()))

M = int(input())
Integer = list(map(int, input().split()))

answer = []

for i in Integer:
    answer.append(1 if i in myCards else 0)

print(*answer)
