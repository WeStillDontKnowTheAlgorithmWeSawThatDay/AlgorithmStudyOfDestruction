import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

start, end = 0, N - 1
answer = [arr[start], arr[end]]


while start < end:
    tmp = arr[start] + arr[end]
    if abs(tmp) < abs(sum(answer)):
        answer = [arr[start], arr[end]]
        if tmp == 0:
            break
    if tmp < 0:
        start += 1
    else:
        end -= 1

print(*sorted(answer))
