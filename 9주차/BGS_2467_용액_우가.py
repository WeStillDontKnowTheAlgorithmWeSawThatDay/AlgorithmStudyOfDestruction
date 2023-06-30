def test():
    n = int(input())
    lis = list(map(int, input().split()))

    answer = []
    tempLeft = 0
    tempRight = n - 1

    minYong = 1999999999
    while tempLeft < tempRight:
        yong = lis[tempLeft] + lis[tempRight]

        if abs(yong) < minYong:
            temp = []
            temp.append(lis[tempLeft])
            temp.append(lis[tempRight])
            answer = temp
            minYong = abs(yong)

        if yong < 0:
            tempLeft += 1
        if yong > 0:
            tempRight -= 1
        if yong == 0:
            break

    print(answer[0], answer[1])

test()
