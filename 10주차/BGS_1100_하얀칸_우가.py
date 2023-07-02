arr = []
for i in range(8):
    arr.append(input())

# 00 11
# 02 13
# 04 15
# 06 17
cnt = 0
for idx, s in enumerate(arr):
    if idx % 2 == 0:
        if s[0] == 'F':
            cnt += 1
        if s[2] == 'F':
            cnt += 1
        if s[4] == 'F':
            cnt += 1
        if s[6] == 'F':
            cnt += 1
    else:
        if s[1] == 'F':
            cnt += 1
        if s[3] == 'F':
            cnt += 1
        if s[5] == 'F':
            cnt += 1
        if s[7] == 'F':
            cnt += 1

print(cnt)