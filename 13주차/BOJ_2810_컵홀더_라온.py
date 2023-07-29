n = int(input())
seats = list(input())

answer = 0
while seats:
    answer += 1
    if seats[-1] == 'L':
        seats.pop()
        seats.pop()
    else:
        seats.pop()

if answer >= n:
    print(n)
else:
    print(answer+1)