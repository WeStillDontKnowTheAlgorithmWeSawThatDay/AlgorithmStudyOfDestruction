n = int(input())
for i in range(2*n):
    if i < n:
        print(" "*i + "*"*(2*(n-i)-1))
    if i > n:
        print(" "*(2*n-i-1) + "*"*(2*(i-n+1)-1))
