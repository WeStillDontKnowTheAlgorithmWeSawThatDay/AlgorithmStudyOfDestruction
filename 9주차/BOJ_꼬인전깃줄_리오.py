n = int(input())
array = list(map(int, input().split()))
d = [n+1] * (n+1)
d[1] = array[0]
for x in array[1:]:
    start = 1
    end = n + 1
    index = 0
    while start <= end:
        mid = (start + end) // 2
        if d[mid] < x:
            index = max(index, mid)
            start = mid + 1
        else:
            end = mid - 1

    d[index + 1] = x

for i in range(1, n + 1):
    if d[i] == n + 1:
        break
print(n - (i - 1))
