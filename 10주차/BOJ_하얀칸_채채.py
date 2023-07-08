chess = []
answer = 0

for i in range(8):
    chess.append(input())

for i in range(8):
    for j in range(8):
        if (i %2 == 0 and j%2 == 0) or (i %2 != 0 and j%2 != 0):
            if chess[i][j] == "F":
                answer += 1
print(answer)
