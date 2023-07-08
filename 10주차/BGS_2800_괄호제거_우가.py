import itertools
s = str(input())

stk = []
temp = []
for i, e in enumerate(s):
    if e == '(':
        stk.append(i)
    elif e == ')':
        d = stk.pop()
        l = []
        l.append(d)
        l.append(i)
        temp.append(l)
i = 1

answer = set()
for i in range(1, len(temp) + 1):
    for k in itertools.combinations(temp, i):
        ttttt = ''
        temps = []
        for kk in k:
            x, y = kk
            temps.append(x)
            temps.append(y)
        
        for jjj in range(len(s)):
            if jjj in temps:
                continue
            ttttt += s[jjj]
        answer.add(ttttt)

for k in sorted(answer):
    print(k)
