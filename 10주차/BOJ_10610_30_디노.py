# 30 -> 2, 3, 5 의 공배수

numList = list(input())
numList.sort(reverse=True)

num_sum = 0
for n in numList:
    num_sum += int(n)

if numList[-1] != '0' or num_sum % 3 != 0:
    print(-1)
else:
    print(''.join(numList))
