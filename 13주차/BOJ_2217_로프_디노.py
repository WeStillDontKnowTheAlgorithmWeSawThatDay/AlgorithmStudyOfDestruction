N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort()

ans = 0
for i in range(len(rope)):
    # print(rope[i], len(rope) - i)
    ans = max(ans, rope[i] * (len(rope) - i))

print(ans)
