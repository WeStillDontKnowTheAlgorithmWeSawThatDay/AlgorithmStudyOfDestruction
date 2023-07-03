chess = []
for _ in range(8):
    chess.append(input())

temp = 0
count = 0
for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if temp % 2 == 0 and chess[i][j] == 'F':
                count += 1
            temp += 1
        else:
            if temp % 2 == 1 and chess[i][j] == 'F':
                count += 1
            temp += 1

print(count)