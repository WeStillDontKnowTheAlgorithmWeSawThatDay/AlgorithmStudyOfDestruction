def func1(n):
    answer = 1
    for i in range(n, int(n/2)+1, -1):
        answer *= i
    return answer

def func2(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer

while True:
    n = int(input())
    if n == 0:
        break
    print(int(func1(2*n)/func2(n)))
