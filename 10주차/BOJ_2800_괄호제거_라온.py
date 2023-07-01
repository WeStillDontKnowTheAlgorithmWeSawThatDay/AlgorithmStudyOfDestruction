import copy
from itertools import *

formula = list(input())
open, close = [], {}

stack = []
    
for i, ch in enumerate(formula):
    if ch == '(':
        stack.append(i)
        open.append(i)
        
    if ch == ')':
        temp = stack[len(stack)-1]
        close[temp] = i
        stack.pop()

# print(open)
# print(close)

nums = [i for i in range(len(open))]
cases = []
for i in range(1, len(open)+1):
    combs = list(combinations(nums, i))
    for comb in combs:
        cases.append(comb)

# print(cases)
answer = []
for case in cases:
    removes = []
    for i in case:
        removes.append(open[i])
        removes.append(close[open[i]])
    removes.sort(reverse=True)
    temp = copy.deepcopy(formula)
    for remove in removes:
        del temp[remove]
    answer.append(''.join(temp))
answer = list(set(answer))
answer.sort()
for ans in answer:
    print(ans)

# 1, 2, 3, 12, 13, 23, 123
# ((((1))))(2)
