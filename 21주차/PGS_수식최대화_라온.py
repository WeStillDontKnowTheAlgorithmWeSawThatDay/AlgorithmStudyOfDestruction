import re
from collections import deque
import copy
import itertools

def calculate(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '*':
        return operand1 * operand2
    if operator == '-':
        return operand1 - operand2
        
def case(expression, operators):
    tokens = copy.deepcopy(expression)
    
    operand1 = int(tokens.popleft())
    temp = deque([operand1])
    n = 0
    while n <= 2:
        current = operators[n]
        
        operand1 = temp.pop()
        operator = tokens.popleft()
        operand2 = int(tokens.popleft())        
        if operator == current:
            result = calculate(operator, operand1, operand2)
            temp.append(result)
        else:
            temp.append(operand1)
            temp.append(operator)
            temp.append(operand2)
        if len(tokens) == 0 and len(temp) <= 1:
            break
            
        if len(tokens) <= 1:
            tokens = copy.deepcopy(temp)
            temp.clear()
            temp.append(int(tokens.popleft()))
            n += 1
    return abs(temp[0])
    
def solution(expression):
    answer = []
    expression = re.split(r'([-+*/])', expression)
    expression = deque(expression)
    
    operator_kind = ['*', '+', '-']
    operator_kinds = itertools.permutations(operator_kind, 3)
    
    for operators in list(operator_kinds):
        result = case(expression, operators)
        answer.append(result)
    return max(answer)





