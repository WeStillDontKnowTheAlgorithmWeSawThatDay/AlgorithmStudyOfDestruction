import sys
import math

input = sys.stdin.readline
factorial = math.factorial

for _ in range(int(input())):
    n, m = map(int, input().split())
    answer = factorial(m) // (factorial(n) * factorial(m - n))
    print(answer)
