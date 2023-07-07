l = list(map(int,input()))

if 0 not in l :
    print(-1)
elif l == [0] :
    print(-1)
else :
    l.remove(0)
    l.sort(reverse=True)
    s = sum(l)
    if s % 3 == 0 :
        if sum(l)//3 ==0 :
            print(-1)
        else :
            print(int(''.join(str(p) for p in l) +'0'))
    else :
        print(-1)
