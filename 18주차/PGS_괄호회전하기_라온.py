from collections import deque

def is_bracket(s):
    stack = []
    for ch in s:
        if not stack and (ch == ']' or ch == ')' or ch == '}'): 
            # stack is empty and closed bracket
            return False
        
        if ch == '[' or ch == '(' or ch == '{':
            # opened bracket
            stack.append(ch)
        if ch == ']' and stack[-1] == '[':
            stack.pop()
        elif ch == ')' and stack[-1] == '(':
            stack.pop()
        elif ch == '}' and stack[-1] == '{':
            stack.pop()
    return not stack

def solution(s):
    answer = 0
    queue = deque(s)
    n = 0
    while n < len(s):
        if is_bracket(queue):
            answer += 1
        queue.append(queue.popleft())
        n += 1
    return answer
