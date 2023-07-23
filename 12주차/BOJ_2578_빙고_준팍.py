import sys

input = sys.stdin.readline

def check_bingo(bingo):
    cnt = 0
    # 행 확인
    for row in bingo:
        if sum(row) == 5:
            cnt += 1
    # 열 확인
    for col in zip(*bingo):
        if sum(col) == 5:
            cnt += 1
    # 대각선 확인
    if sum(bingo[i][i] for i in range(5)) == 5:
        cnt += 1
    if sum(bingo[i][4-i] for i in range(5)) == 5:
        cnt += 1
    return cnt >= 3

board = [list(map(int, input().split())) for _ in range(5)]
lines = [list(map(int, input().split())) for _ in range(5)]

bingo = [[0] * 5 for _ in range(5)]

# 숫자별 좌표 찾기
num_map = {board[i][j]: (i, j) for i in range(5) for j in range(5)}

count = 0

for line in lines:
    for num in line:
        count += 1
        x, y = num_map[num]
        bingo[x][y] = 1
        if check_bingo(bingo):
            print(count)
            sys.exit(0)  # 빙고를 외치면 프로그램을 종료합니다.
