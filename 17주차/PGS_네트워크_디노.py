def solution(n, computers):
    chk = [0 for _ in range(n)]
    cnt = 0

    for i in range(n):
        if chk[i] == 0:
            cnt += 1
            # print("chk[i] = ", i, chk[i])
            chk[i] = 1
            stack = [i]
            while stack:
                # print("stack", stack)
                now = stack.pop()
                for d in range(n):
                    if computers[now][d] == 1 and chk[d] == 0:  # i 말고 now로 ...
                        chk[d] = 1
                        stack.append(d)

    return cnt
