import sys
input = sys.stdin.readline

S = input().strip()
switches = sum(s1 != s2 for s1, s2 in zip(S, S[1:]))
flips = (switches + 1) // 2

print(flips)
