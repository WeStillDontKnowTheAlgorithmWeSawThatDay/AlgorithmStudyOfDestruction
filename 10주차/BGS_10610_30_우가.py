n = input()
arr = list(n)
arr.sort(reverse=True)

if int(''.join(arr)) % 30 == 0:
    print(''.join(arr))
else:
    print(-1)