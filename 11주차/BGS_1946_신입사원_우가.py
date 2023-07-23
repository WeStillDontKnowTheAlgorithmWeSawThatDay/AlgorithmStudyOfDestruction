import sys
n = int(sys.stdin.readline())

for _ in range(n):
    i = int(sys.stdin.readline())
    temp = []
    for __ in range(i):
        a, b = map(int, sys.stdin.readline().split())
        temp.append([a, b])
    temp.sort()
    cnt = 1

    comp = temp[0][1]
    for j in range(1, i):
        if temp[j][1] < comp:
            comp = temp[j][1]
            cnt += 1
    print(cnt)
