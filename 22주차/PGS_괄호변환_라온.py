from collections import deque

def calculate(bracket, num):
    if bracket == '(':  num += 1
    else:   num -= 1
    return num

def find_balance(p):
    stack = []
    queue, num = deque(p), 0
    bracket = queue.popleft()
    stack.append(bracket)
    num = calculate(bracket, num)
    while queue and num != 0:
        bracket = queue.popleft()
        stack.append(bracket)
        num = calculate(bracket, num)
    return ''.join(stack), ''.join(queue)

def is_right(p):
    stack, queue = [], deque(p)
    bracket = queue.popleft()
    if bracket != '(':
        return False
    while queue and stack:
        bracket = queue.popleft()
        if bracket == '(':
            stack.append('(')
        else:
            stack.pop()
    return not stack # empty -> True
    
def reverse(p):
    queue = deque(p)
    stack = []
    while queue:
        bracket = queue.popleft()
        if bracket == '(':
            stack.append(')')
        else:
            stack.append('(')
    return ''.join(stack)


def solution(p):
    if p == '':
        return p
    u, v = find_balance(p)
    print("u = ", u, "v = ", v)
    if is_right(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse(u[1:len(u)-1])

''' 이전 풀이'''
def is_stack(p):
    stack = []
    for bracket in p:
        if bracket == "(":  stack.append(bracket)
        else:
            if len(stack) == 0: return False
            stack.pop()
    if len(stack) == 0: return True

def balance(p):
    bal_p = ""
    bal_num = 0
    for bracket in p:
        bal_p += bracket
        if bracket == "(":  bal_num += 1
        else:   bal_num -= 1
        if bal_num == 0:    break
    return bal_p

def solution(p):
    answer = ''
    if is_stack(p):  return p
    else:
        u = balance(p)
        v = p[len(u):]
        # print("u, v:", u, v)
        if is_stack(u):
            answer += u + solution(v)
        else:
            string = "(" + solution(v) + ")"
            temp = u[1:len(u)-1]
            temp = temp.replace("(", "0").replace(")", "(").replace("0", ")")

            return string + temp
    return answer