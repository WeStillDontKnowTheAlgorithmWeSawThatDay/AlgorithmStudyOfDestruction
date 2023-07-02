l = [list(input()) for _ in range(8)]
answer = 0
for a in range(8) :
    for b in range(8) :
        if (a+b) % 2 == 0 :
            if l[a][b] == 'F' :
                answer += 1

print(answer)
