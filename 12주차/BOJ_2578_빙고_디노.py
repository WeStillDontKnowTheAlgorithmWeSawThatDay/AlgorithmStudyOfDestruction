def chkBingo(chk):
    cnt = 0
    for i in range(5):
        if sum(chk[i]) == 5:
            cnt += 1
    for j in range(5):
        if chk[0][j] + chk[1][j] + chk[2][j] + chk[3][j] + chk[4][j] == 5:
            cnt += 1
    if chk[0][0] + chk[1][1] + chk[2][2] + chk[3][3] + chk[4][4] == 5:
        cnt += 1
    if chk[0][4] + chk[1][3] + chk[2][2] + chk[3][1] + chk[4][0] == 5:
        cnt += 1
    if cnt >= 3:
        return True
    else:
        return False


arr = [list(map(int, input().split())) for _ in range(5)]
chk = [[0] * 5 for _ in range(5)]

cnt = 0
for _ in range(5):
    call = list(map(int, input().split()))
    for c in call:
        cnt += 1
        for i in range(5):
            for j in range(5):
                if arr[i][j] == c:
                    chk[i][j] = 1

        if chkBingo(chk):
            print(cnt)
            exit(0)

print(arr)
print(chk)
