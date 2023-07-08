x = input()
y = input()
answer = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
max_answer = 0
for i in range(1,len(x)+1):
    for j in range(1,len(y)+1):
        if x[i-1] == y[j-1]:
            answer[i][j] = answer[i-1][j-1] +1
            max_answer = max(answer[i][j],max_answer)

print(max_answer)
