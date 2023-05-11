def solution(n):
    l1 = [0, 1]
    l2 = []

    while n != 0 :
        a = (l1[-1] + l1[-2])%1234567
        l2.append(a)
        l1.append(a)
        n -= 1
    answer = l2[n-2]
    return answer
