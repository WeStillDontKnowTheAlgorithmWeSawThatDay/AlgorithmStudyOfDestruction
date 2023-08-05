# **, 어려워어려워어려워, 다시 풀어봐야돼, sys 해줘야함
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
weights = [list(map(int, input().split())) for _ in range(e)]

weights.sort(key=lambda x: x[2])
parents = [i for i in range(v+1)]

def find_parent(x):
    if parents[x] == x:
        return x
    parents[x] = find_parent(parents[x])
    return parents[x]

def union(i, j):
    i = find_parent(i)
    j = find_parent(j)

    if i < j:
        parents[j] = i
    else:
        parents[i] = j

ans = 0
for i, j, w in weights:
    if find_parent(i) != find_parent(j):    
        union(i, j)
        ans += w
print(ans)
