T = int(input())

def func(num):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num
    
for _ in range(T):
    n, m = map(int, input().split())
    print(func(m) // (func(n) * func(m-n)))
