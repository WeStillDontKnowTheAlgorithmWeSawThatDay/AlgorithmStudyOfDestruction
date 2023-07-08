x = input()
y = input()
z = input()
answer = [[[0] * (len(z) + 1) for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
max_answer = 0
for i in range(1,len(x)+1):
    for j in range(1,len(y)+1):
        for k in range(1,len(z)+1):
            if x[i-1] == y[j-1] and y[j-1] == z[k-1]:
                answer[i][j][k] = answer[i-1][j-1][k-1] +1
                max_answer = max(answer[i][j][k],max_answer)
            else:
                answer[i][j][k]+=max(answer[i-1][j][k],answer[i][j-1][k],answer[i][j][k-1])

print(max_answer)
