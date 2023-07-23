import sys

input = sys.stdin.readline

paper = [[0]*100 for _ in range(100)]  # 도화지를 초기화
area = 0  # 검은색 영역의 넓이

for _ in range(int(input())):
    n, m = map(int, input().split())
    for x in range(n, n + 10):
        for y in range(m, m + 10):
            if paper[x][y] == 0:
                paper[x][y] = 1
                area += 1

print(area)
