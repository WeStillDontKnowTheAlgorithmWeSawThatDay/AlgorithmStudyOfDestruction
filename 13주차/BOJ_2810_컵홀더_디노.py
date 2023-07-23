N = int(input())
info = input()

cou = 0
cnt = 1
for i in info:
    if i == 'S':
        cnt += 1
    if i == 'L' and cou == 0:
        cou = 1
        continue
    if i == 'L' and cou == 1:
        cnt += 1
        cou = 0

if N > cnt:
    print(cnt)
else:
    print(N)