def solution(line):
    s = set()
    for a in line :
        for b in line :
            z = a[0]*b[1] - a[1]*b[0]
            if z == 0 :
                continue;
            x = (a[1]*b[2] - a[2]*b[1])/(z)
            y = (a[2]*b[0] - a[0]*b[2])/(z)
            if int(x) == x and int(y) == y :
                s.add((int(x),int(y)))

    minx = 9999999987654321
    maxx = -999999987654321
    miny = 9999999987654321
    maxy = -9999999987654321

    for t in s :
        if t[0] < minx :
            minx = t[0]
        if t[1] < miny :
            miny = t[1]
        if t[0] > maxx :
            maxx = t[0]
        if t[1] > maxy :
            maxy = t[1]

    answer = ["."*(maxx - minx + 1)]*(maxy - miny + 1)

    for tt in s :
        yy = tt[1]-miny
        l = list(answer[yy])
        l[tt[0]-minx] = "*"
        answer[tt[1]-miny] = ''.join(l)
    answer.reverse()
    return answer
