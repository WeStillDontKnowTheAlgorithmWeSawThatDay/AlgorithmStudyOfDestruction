import sys

input = sys.stdin.readline

def max_sequence_sum(sequence):
    positive = sorted([x for x in sequence if x > 1])
    negative = sorted([x for x in sequence if x < 0], reverse=True)
    ones = [x for x in sequence if x == 1]  # 1은 곱하는 것보다 더하는 것이 유리
    zeros = [x for x in sequence if x == 0]  # 0은 음수를 없앨 수 있음

    result = sum(ones)  # 1은 곱하는 것보다 더하는 것이 유리하므로 미리 합에 더함

    # 양수 묶기
    while len(positive) > 1:
        result += positive.pop() * positive.pop()

    # 음수 묶기
    while len(negative) > 1:
        result += negative.pop() * negative.pop()

    # 남은 양수 더하기
    if positive:
        result += positive[0]

    # 남은 음수 더하기 (0이 있으면 제거)
    if negative and len(zeros) == 0:
        result += negative[0]

    return result

print(max_sequence_sum([int(input()) for _ in range(int(input()))]))
