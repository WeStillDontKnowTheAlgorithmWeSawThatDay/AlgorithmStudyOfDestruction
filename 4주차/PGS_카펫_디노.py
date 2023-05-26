def solution(brown, yellow):
    x = 3
    while True:
        y = yellow / (x-2) + 2
        if (x+y-2) *2 == brown and (x-2)*(y-2) == yellow:
            return [y, x]
        x += 1

# 수학