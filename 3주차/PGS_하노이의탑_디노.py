answer = []

def hanoi(n, start, mid, end):
    if n == 1:
        answer.append([start, end])
    else:
        hanoi(n - 1, start, end, mid)
        answer.append([start, end])
        hanoi(n - 1, mid, start, end)

def solution(n):
    hanoi(n, 1, 2, 3)
    return answer

# def solution(n):
#     return hanoi(n, 1, 3)
#
# def hanoi(n, a, b): # n개, a -> b
#     if n == 0: return []
#     return hanoi(n-1, a, 6-(a+b))+[[a, b]]+hanoi(n-1, 6-(a+b), b)
