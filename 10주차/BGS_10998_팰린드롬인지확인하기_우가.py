st = input()

if len(st) == 1:
    print(1)
    exit()
for i in range(len(st)//2):
    if st[i] != st[len(st) - i - 1]:
        print(0)
        break
    else:
        if i == len(st)//2 - 1:
            print(1)
