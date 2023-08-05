import sys

input = sys.stdin.readline

N = i = int(input())

while i > 1-N:
    i -= 1
    x = abs(i) + 1
    print(' ' * (N - x) + '*' * (2*x - 1))
