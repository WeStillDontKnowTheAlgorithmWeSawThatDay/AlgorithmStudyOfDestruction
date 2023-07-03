# 답은 잘 나오나 메모리 초과
# 10^5개의 숫자를 순열로 구하려니깐 메모리 초과가 발생하는 걸로 보임
#
# from itertools import permutations
#
# num = input()
#
# temp = list(permutations(num, len(num)))
#
# answer = []
# for i in temp:
#     pos = int(''.join(i))
#     if pos % 30 == 0:
#         answer.append(pos)
#
# if len(answer) == 0:
#     print(-1)
# else:
#     print(max(answer))

num = ''.join(sorted(input(), reverse=True))

sum = 0
for i in num:
    sum += int(i)

if sum % 3 == 0 and int(num[len(num)-1]) == 0:
    print(num)
else:
    print(-1)
