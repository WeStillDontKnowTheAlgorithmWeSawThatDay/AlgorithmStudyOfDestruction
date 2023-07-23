from collections import deque

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]

ans = 0

# visited =[[0] * n for _ in range(m)]
# queue = deque()
# queue.append((0, 0))

def func(answer, stack):
    i, j = stack[-1]
    if (i, j) == (m-1, n-1):
        # print(stack)
        answer += 1
        return answer
    for dir in dirs:
        x, y = i + dir[0], j + dir[1]
        if 0 <= x < m and 0 <= y < n and maps[x][y] < maps[i][j]:
            if (x, y) not in stack:
                stack.append((x, y))
                # print(stack)
                answer = func(answer, stack)
    stack.pop()
    return answer


stack = [(0, 0)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
print(func(ans, stack))
