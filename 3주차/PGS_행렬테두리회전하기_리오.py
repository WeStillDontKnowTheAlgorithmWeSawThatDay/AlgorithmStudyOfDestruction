def solution(rows, columns, queries):
    l = []
    answer = []
    for k in range(rows) :
        ll = []
        for kk in range(1, columns + 1) :
            ll.append(k*columns + kk)
        l.append(ll)

    for ay,ax,by,bx in queries :
        min = 987654321
        a1 = l[ay-1][ax-1]
        for i in range(ay-1, by-1) :
            if l[i+1][ax-1] < min :
                min = l[i+1][ax-1]
            l[i][ax-1] = l[i+1][ax-1]
        for ii in range(ax-1, bx-1) :
            if l[by-1][ii+1] < min :
                min = l[by-1][ii+1]
            l[by-1][ii] = l[by-1][ii+1]
        for iii in range(by-1, ay-1, -1) :
            if l[iii-1][bx-1] < min :
                min = l[iii-1][bx-1]
            l[iii][bx-1] = l[iii-1][bx-1]
        for iiii in range(bx-1, ax-1, -1) :
            if l[ay-1][iiii-1] < min :
                min = l[ay-1][iiii-1]
            l[ay-1][iiii] = l[ay-1][iiii-1]
        l[ay-1][ax] = a1
        if a1 < min :
            min = a1
        answer.append(min)

    return answer
