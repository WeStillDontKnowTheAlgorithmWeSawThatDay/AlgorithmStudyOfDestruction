n = int(input())
for i in range(n) :
    a,b = map(int,input().split())
    c = 1
    d = 1
    for ii in range(1,a+1) :
        c *= (b-ii+1)
        d *= ii
    print(c//d)
