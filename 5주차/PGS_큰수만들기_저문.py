from itertools import combinations

def solution(number, k):
    answer = ''
    stack = []
    index = 0
    while len(stack) != 4:
        if len(stack) == 0:
            stack.append(number[index])
            continue
        if stack[-1] < number[index]:
            stack.append(number[index])
        print(stack)

        index += 1

    return answer