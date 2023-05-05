def cal(finger, target):
    return abs(finger[0] - target[0]) + abs(finger[1] - target[1])


def solution(numbers, hand):
    answer = ''
    left, right = [0, 0], [0, 2]
    keypad = {}

    keypad[0] = [0, 1]

    keypad[7] = [1, 0]
    keypad[8] = [1, 1]
    keypad[9] = [1, 2]

    keypad[4] = [2, 0]
    keypad[5] = [2, 1]
    keypad[6] = [2, 2]

    keypad[1] = [3, 0]
    keypad[2] = [3, 1]
    keypad[3] = [3, 2]

    for n in numbers:
        if n in [1, 4, 7]:
            left = keypad[n]
            answer += 'L'
        elif n in [3, 6, 9]:
            right = keypad[n]
            answer += 'R'
        else:
            if cal(left, keypad[n]) < cal(right, keypad[n]):
                left = keypad[n]
                answer += 'L'
            elif cal(left, keypad[n]) > cal(right, keypad[n]):
                right = keypad[n]
                answer += 'R'
            else:
                if hand == 'left':
                    left = keypad[n]
                    answer += 'L'
                else:
                    right = keypad[n]
                    answer += 'R'

    return answer
