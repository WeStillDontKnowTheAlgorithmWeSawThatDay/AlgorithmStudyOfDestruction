import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().rsplit()))

l, r, curr, answer = 0, n-1, 0, sys.maxsize
ansl, ansr = 0, 0

while l < r:
    if abs(data[l] + data[r]) < answer:
        answer = abs(data[l] + data[r])
        ansl, ansr = data[l], data[r]

    if data[l] + data[r] < 0:
        l += 1
    else:
        r -= 1

print(ansl, ansr)
