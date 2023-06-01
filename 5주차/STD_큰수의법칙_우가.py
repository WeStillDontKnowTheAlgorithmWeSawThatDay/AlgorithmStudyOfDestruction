n, m, k= map(int, input().split())
data = list(map(int, input().split()))
maxx = max(data)
ss = data
ss.remove(maxx)
ssxx = max(ss)

ans = 0
while m != 0:
    for _ in range(k):
        ans += maxx
        m -= 1
    ans += ssxx
    m -= 1
    
print(ans)