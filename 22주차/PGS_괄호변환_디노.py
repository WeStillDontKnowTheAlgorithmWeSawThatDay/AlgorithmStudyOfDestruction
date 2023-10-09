def isBalanced(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    # 1
    if not p:
        return ""

    # 2
    l_cnt = 0
    r_cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            l_cnt += 1
        elif p[i] == ')':
            r_cnt += 1
        if l_cnt == r_cnt:
            u, v = p[:i + 1], p[i + 1:]
            break

    # 3
    if isBalanced(u):
        return u + solution(v)
    # 4
    else:
        answer = '(' + solution(v) + ')'

        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer
