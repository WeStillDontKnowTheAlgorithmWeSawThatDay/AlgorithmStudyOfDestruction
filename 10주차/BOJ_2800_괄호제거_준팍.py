import sys
from itertools import combinations

def remove_bracket(expr, brackets):
    new_expr = list(expr)
    for i in brackets:
        new_expr[i] = ''
    return ''.join(new_expr)

def solve():
    expr = sys.stdin.readline().strip()
    brackets = []
    stack = []
    for i in range(len(expr)):
        if expr[i] == '(':
            stack.append(i)
        elif expr[i] == ')':
            brackets.append((stack.pop(), i))

    brackets.sort(reverse=True)
    results = set()

    for i in range(1, len(brackets) + 1):
        for comb in combinations(brackets, i):
            results.add(remove_bracket(expr, [j for i in comb for j in i]))

    results = sorted(list(results))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
