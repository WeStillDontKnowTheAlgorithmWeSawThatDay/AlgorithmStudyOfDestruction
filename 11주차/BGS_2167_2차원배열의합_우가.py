import sys
x, y = map(int, sys.stdin.readline().split())
arr = []
for xx in range(x):
    temp = []
    for yy in list(map(int, sys.stdin.readline().split())):
        temp.append(yy)
    arr.append(temp)

case = int(input())
for _ in range(case):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    sum = 0
    for xx in range(x1-1, x2):
        for yy in range(y1-1, y2):
            sum += arr[xx][yy]
    print(sum)
