mov = [(1, 0), (0, 1), (-1, -1)]


def is_possible(n, x, y):
    return 0 <= x < n and 0 <= y <= x


def solution(n):
    answer = [[1]]
    for i in range(2, n + 1):
        answer.append([0 for _ in range(i)])

    x, y = 0, 0
    way = 0
    for cnt in range(2, n * (n + 1) // 2 + 1):
        while True:
            nx, ny = x + mov[way][0], y + mov[way][1]
            if is_possible(n, nx, ny) and answer[nx][ny] == 0:
                answer[nx][ny] = cnt
                x, y = nx, ny
                break
            else:
                way += 1
                way %= 3

    new_ans = []
    for ans in answer:
        for a in ans:
            new_ans.append(a)
    return new_ans

# 1
# 2  15
# 3  16  14
# 4  17  21  13
# 5  18  19  20 12       [4,4]
# 6  7   8   9  10  11   [5,5]

# 1. 밑으로
# 2. 오른쪽으로
# 3. 대각선 좌상단