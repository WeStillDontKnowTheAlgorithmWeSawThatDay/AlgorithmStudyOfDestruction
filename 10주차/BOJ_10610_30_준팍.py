import sys

input = sys.stdin.readline

items = [int(n) for n in input().rstrip()]

# 30의 배수를 찾기 위한 조건 확인
if sum(items) % 3 != 0 or 0 not in items:
    print(-1)
else:
    # 30의 배수를 만들 수 있는 경우, 숫자를 내림차순으로 정렬하여 가장 큰 수를 만듬
    items.sort(reverse=True)
    print(''.join(map(str, items)))


# 메모리 초과버전
# import sys
# from itertools import permutations

# input = sys.stdin.readline

# items = [int(n) for n in input().rstrip()]

# arr = list(permutations(items, len(items)))

# results = []

# for a in arr :
#     b = int(''.join(map(str, a)))
#     if b % 30 == 0:
#          results.append(b)


# if len(results) == 0 :
#      print(-1)
# else :
#      print(max(results))