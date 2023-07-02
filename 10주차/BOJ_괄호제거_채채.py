from itertools import combinations

data = list(input())

x = []
couple = []
result = set()
for i in range(len(data)):
    if data[i] == '(':
        x.append(i)
    elif data[i] == ')':
        couple.append((x.pop(),i))

for i in range(1, len(couple)+1):
    com = list(combinations(couple, i)) 
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
