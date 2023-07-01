chess = []
for _ in range(8):
    line = list(input())
    chess.append(line)

num = 0
for i in range(8):
    for j in range(8):
        if i%2 == 0 and j%2 == 0 and chess[i][j] == 'F':
            num += 1
        if i%2 == 1 and j%2 == 1 and chess[i][j] == 'F':
            num += 1
print(num)