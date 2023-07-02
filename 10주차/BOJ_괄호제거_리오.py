from itertools import combinations

data = list(input())

stack = []
index = []
result = set()
for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)
    elif data[i] == ')':
        index.append((stack.pop(),i))

for i in range(1, len(index)+1):
    com = list(combinations(index, i))
    for c in com:
        temp = data[:]
        for x,y in c:
            temp[x] = ''
            temp[y] = ''
        result.add(''.join(temp))

result = list(result)
result.sort()
for i in result:
    print(i)
