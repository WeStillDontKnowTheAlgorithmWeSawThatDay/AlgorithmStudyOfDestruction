import math

num = int(input())
case = []
for _ in range(num):
    n, m = map(int, input().strip().split())
    case.append([n, m])

for i in range(len(case)):
    print(math.comb(case[i][1], case[i][0]))
