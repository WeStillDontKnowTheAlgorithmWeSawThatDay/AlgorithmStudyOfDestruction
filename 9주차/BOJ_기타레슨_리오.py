n,m = map(int,input().split())

l = list(map(int,input().split()))

num = sum(l)

start = max(l)
end = sum(l)
result = num

while start<=end:
    mid = (start+end) // 2
    if mid < max(l):
        start = mid + 1
        continue

    cnt,tmp =1,0

    for i in range(len(l)):
        if tmp + l[i] <= mid:
            tmp += l[i]
        else:
            tmp = l[i]
            cnt += 1

    if cnt <= m:
        end = mid - 1
        result = min(result,mid)
    else:
        start = mid + 1

print(result)
