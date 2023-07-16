import sys
input = sys.stdin.readline
t = int(input())
for test in range(t) :
    n = int(input())
    l = []
    for num in range(n) :
        l.append(list(map(int,input().split())))
    l.sort()
    a = l[0][1]
    cnt = 1
    for i in range(1,n) :
        if l[i][1] < a :
            cnt += 1
            a = l[i][1]
    print(cnt)
