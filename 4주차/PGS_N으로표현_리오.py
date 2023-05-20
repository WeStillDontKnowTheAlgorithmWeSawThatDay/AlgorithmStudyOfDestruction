def solution(N, number):
    if number == 1:
        return 1

    l = []

    for a in range(1, 9):
        s = set()
        s.add(int(str(N) * a))

        for i in range(a - 1):
            for x in l[i]:
                for y in l[-i-1]:
                    s.add(x + y)
                    s.add(x * y)
                    s.add(x - y)
                    if y != 0:
                        s.add(x / y)

        if number in s:
            return a

        l.append(s)

    return -1
