def hanoi(frm, to, mid, n, answer):
    if n == 1:
        answer.append([frm, to])
        return
    hanoi(frm, mid, to, n - 1, answer)
    answer.append([frm, to])
    hanoi(mid, to, frm, n - 1, answer)

def solution(n):
    answer = []
    hanoi(1, 3, 2, n, answer)
    return answer
