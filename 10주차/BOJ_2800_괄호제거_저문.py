from itertools import combinations

ex = input()

# 괄호 쌍의 인덱스를 모두 찾기
index = []
stack = []
for i, s in enumerate(ex):
    if s == '(':
        stack.append(i)
    elif s == ')':
        start = stack.pop()
        end = i
        index.append([start, end])

# 해당 인덱스로 만들 수 있는 모든 조합 찾기
answer = []
for i in range(1, len(index)+1):
    for j in combinations(index, i):
        temp = list(ex)
        for k in j:
            start, end = k
            temp[start] = ''
            temp[end] = ''
        answer.append(''.join(temp))

for s in sorted(list(set(answer))):
    print(s)
