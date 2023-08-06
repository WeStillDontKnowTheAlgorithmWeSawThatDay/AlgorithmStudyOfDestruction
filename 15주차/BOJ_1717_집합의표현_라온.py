# readline이랑 recursionlimit 설정해줘야됨

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = []
for i in range(n+1):
    parent.append(i)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    cond, a, b = map(int, input().split())
    if cond == 0:
        union(a, b)
    if cond == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    