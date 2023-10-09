N = int(input())
home = list(map(int, input().split()))

cnt = 0

while cnt < 1440:
    home.sort(reverse=True)
    tmp = 0
    cnt += 1
    for i in range(len(home)):
        if home[i] > 0:
            home[i] -= 1
            tmp += 1
        if tmp == 2:
            break
    if sum(home) == 0:
        print(cnt)
        exit(0)
    # print(home)


print(-1)
