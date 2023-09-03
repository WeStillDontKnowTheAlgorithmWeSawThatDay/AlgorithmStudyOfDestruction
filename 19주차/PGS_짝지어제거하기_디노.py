def solution(s):
    answer = -1

    stack = []

    for ss in s:
        if len(stack) == 0:
            stack.append(ss)
            continue
        if stack[-1] == ss:
            stack.pop()
            continue
        stack.append(ss)

    if stack:
        answer = 0
    else:
        answer = 1

    return answer

