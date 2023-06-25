n, m = map(int, input().strip().split())
lectures = list(map(int, input().strip().split()))

start = max(lectures)
end = sum(lectures)

while start <= end:
    mid = (start + end) // 2
    total = 0
    count = 1
    for l in lectures:
        if total + l > mid:
            count += 1
            total = 0
        total += l

    if count <= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
