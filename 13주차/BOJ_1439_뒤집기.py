S = input()
zero, one = 0, 0

now = 3

for s in S:
    if now != s:
        if s == '0':
            zero += 1
        if s == '1':
            one += 1
        now = s

print(min(zero, one))


