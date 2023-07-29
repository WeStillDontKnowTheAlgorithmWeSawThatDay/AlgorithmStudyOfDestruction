import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        u, v = map(int, input().split())
    print(N - 1)