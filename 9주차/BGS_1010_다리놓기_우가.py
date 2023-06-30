import math
t = int(input())

for i in range(t):
    temp = list(map(int, input().split()))
    print(math.comb(temp[1], temp[0]))
