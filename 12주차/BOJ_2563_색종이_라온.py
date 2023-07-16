# 나 능지

num = int(input())
positions = [list(map(int, input().split())) for _ in range(num)]

paper = [[0] * 101 for _ in range(101)]

for x, y in positions:
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1

answer = 0
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            answer += 1
print(answer)
