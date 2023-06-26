n = int(input())
num_set = set()
ll = list(map(int, input().split()))
for i in range(n) :
    num_set.add(ll[i])

m = int(input())
l = list(map(int,input().split()))
ans = []

for ii in range(m) :
    if l[ii] in num_set :
        ans.append(1)
    elif l[ii] not in num_set :
        ans.append(0)

print(*ans)
