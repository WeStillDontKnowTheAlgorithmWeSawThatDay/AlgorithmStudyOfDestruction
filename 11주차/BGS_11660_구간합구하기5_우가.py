import sys
input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[0] * (n+1)]
for _ in range(n):
    nums = [0] + list(map(int, input().split()))
    graph.append(nums)

for row in range(1,n+1):
    for col in range(2,n+1):
        graph[row][col] += graph[row][col-1]

for row in range(2,n+1):
    for col in range(1,n+1):
        graph[row][col] += graph[row-1][col]

answer = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer.append(graph[x2][y2] - graph[x1-1][y2] - graph[x2][y1-1] + graph[x1-1][y1-1])

for ans in answer:
    print(ans)
