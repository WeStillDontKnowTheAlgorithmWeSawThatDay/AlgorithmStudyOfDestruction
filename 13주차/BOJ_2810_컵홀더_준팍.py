import sys

input = sys.stdin.readline

N = int(input())
seats = input()

couples = seats.count('LL')

if (couples <= 1) :
    print(N)
else :
    print(N - couples + 1)
