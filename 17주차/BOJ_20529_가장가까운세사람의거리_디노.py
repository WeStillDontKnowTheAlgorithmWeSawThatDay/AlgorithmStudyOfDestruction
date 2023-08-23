T = int(input())
for _ in range(T):
    N = int(input())
    people = list(map(str, input().split()))
    ans = 12
    if N > 32:
        print(0)
        continue
    for i in range(N):
        for j in range(N):
            for k in range(N):
                cnt = 0

                if i == j or j == k or i == k:
                    continue
                for d in range(4):
                    if people[i][d] != people[j][d]:
                        cnt += 1
                    if people[j][d] != people[k][d]:
                        cnt += 1
                    if people[i][d] != people[k][d]:
                        cnt += 1
                ans = min(cnt, ans)

    print(ans)
