nums = input()

cnt = [0, 0]
before = -1
for num in nums:
    num = int(num)
    if before == -1:
        cnt[num] += 1
    if (before == 0 and num == 1) or (before == 1 and num == 0):
        cnt[num] += 1
    before = num

print(min(cnt))