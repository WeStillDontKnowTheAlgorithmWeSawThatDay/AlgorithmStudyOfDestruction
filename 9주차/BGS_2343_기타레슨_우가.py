def test():
    n, m = input().split()
    lis = list(map(int, input().split()))

    left = max(lis)
    right = sum(lis)

    while left <= right:
        cnt = 0
        file = 0
        mid = (left + right)//2

        for l in lis:  
            if file + l > mid:
                cnt += 1
                file = l
            else:
                file += l
        if file:
            cnt+=1

        if cnt > int(m):
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    print(answer)

test()
