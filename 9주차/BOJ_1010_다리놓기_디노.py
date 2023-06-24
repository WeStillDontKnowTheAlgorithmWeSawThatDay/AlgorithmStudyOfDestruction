def combi(n, m):
    # mCn 만들기
    up, down = 1, 1
    for i in range(m, m-n, -1):
        up *= i

    for i in range(1, n+1):
        down *= i
    return up // down


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(combi(N, M))
