def solution(line):
    answer = []
    points = []
    minX, maxX, minY, maxY = 10000000000, -10000000000, 10000000000, -10000000000
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            validator = A * D - B * C
            if validator == 0:
                continue
            X, Y = (B * F - E * D) / validator, (E * C - A * F) / validator
            if X % 1 == 0 and Y % 1 == 0:
                minX = int(min(minX, X))
                maxX = int(max(maxX, X))
                minY = int(min(minY, Y))
                maxY = int(max(maxY, Y))

                if [X, Y] not in points:
                    points.append([X, Y])

    for j in range(maxY, minY - 1, -1):
        s = ""
        for i in range(minX, maxX + 1):
            if [i, j] in points:
                s += "*"
            else:
                s += "."
        answer.append(s)
    return answer