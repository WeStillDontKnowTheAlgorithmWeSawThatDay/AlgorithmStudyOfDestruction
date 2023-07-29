import copy

n = int(input())
k = int(input())
apples = [tuple(map(int, input().split())) for _ in range(k)]
l = int(input())

times = dict()
for _ in range(l):
    second, direction = input().split()
    times[int(second)] = direction


apple_board = [[0]*n for _ in range(n)]
for x, y in apples:
    apple_board[x-1][y-1] = 1

length = 1
snakes = [(0,0)]
snakes_dir = [0]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
change = [(3, 2), (2, 3), (0, 1,), (1, 0)]

sec = 1
tail = (0, 0)
head = (0, 0)
flag = False
while True:
    # 전진
    for i in range(length):
        if i == length - 1:
            tail = snakes[i]
        a = snakes[i][0] + dirs[snakes_dir[i]][0]
        b = snakes[i][1] + dirs[snakes_dir[i]][1]
        snakes[i] = (a, b)

        # 보드 밖을 나가는 경우
        if snakes[i][0] < 0 or snakes[i][1] < 0 or snakes[i][0] > n-1 or snakes[i][1] > n-1: 
            flag = True
            break
        # 자신의 몸과 닿는 경우
        if len(set(snakes)) < len(snakes): 
            flag = True
            break

    if flag:
        break

    # 사과먹기
    x, y = snakes[0]
    if apple_board[x][y] == 1:
        length += 1
        snakes.append(tail)
        snakes_dir.append(snakes_dir[::-1])
        apple_board[x][y] = 0

    # 자신의 몸과 닿는 경우
    if len(set(snakes)) < len(snakes): 
        break

    
    # 다음 방향 설정
    temp = copy.deepcopy(snakes_dir)
    for j in range(length-1):
        snakes_dir[j+1] = temp[j]
   
    # 방향 전환
    if times.get(sec) != None:
        if times.get(sec) == 'L':
            snakes_dir[0] = change[snakes_dir[0]][0]
        if times.get(sec) == 'D':
            snakes_dir[0] = change[snakes_dir[0]][1]
    sec += 1
print(sec)
