import sys
def solution(line):
    point = []
    for x in range(0, len(line) - 1):
        for y in range(x+1, len(line)):
            a = line[x][0]
            b = line[x][1]
            e = line[x][2]
            c = line[y][0]
            d = line[y][1]
            f = line[y][2]

            if(a*d - b*c == 0):
                continue
            if((b*f-e*d)%(a*d-b*c) != 0):
                continue
            if((e*c-a*f)%(a*d-b*c) != 0):
                continue

            xy = []
            xy.append((b*f-e*d)//(a*d-b*c))
            xy.append((e*c-a*f)//(a*d-b*c))
            point.append(xy)

    maxx = -sys.maxsize - 1
    maxy = -sys.maxsize - 1
    minx = sys.maxsize
    miny = sys.maxsize
    for i in range(0, len(point)):
        maxx = max(point[i][0], maxx)
        maxy = max(point[i][1], maxy)
        minx = min(point[i][0], minx)
        miny = min(point[i][1], miny)

    pointx = maxx - minx
    pointy = maxy - miny
    answer = []
    for j in range(miny, maxy + 1):
        temp = ""
        for i in range(minx, maxx + 1):
            temp = temp + "."
        answer.append(temp)
    for posit in point:
        posit[0] = posit[0] - minx
        posit[1] = posit[1] - miny

    for posit in point:
        aa = list(answer[posit[1]])
        aa[posit[0]] = "*"
        answer[posit[1]] = "".join(aa)

    answer.reverse()
    return answer

a = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(a))