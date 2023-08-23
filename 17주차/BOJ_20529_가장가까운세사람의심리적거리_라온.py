# *, 비둘기집 ~ 몰랐어 ~ 이제 알아야겠지? 
import sys
t = int(input())

def calculate(t1, t2):
    ssum = 0
    for i in range(4):
        if t1[i] != t2[i]:
            ssum += 1
    return ssum

for _ in range(t):
    n = int(input())
    mbtis = input().split()
    if n > 32:
        print(0)
        continue
    ssum = [sys.maxsize for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            for k in range(j+1, n):
                dist1 = calculate(mbtis[i], mbtis[j])
                dist2 = calculate(mbtis[i], mbtis[k])
                dist3 = calculate(mbtis[j], mbtis[k])
                ssum[i] = min(ssum[i], dist1 + dist2 + dist3)
    print(min(ssum))
