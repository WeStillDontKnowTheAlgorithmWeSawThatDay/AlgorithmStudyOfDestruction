def solution(numbers, hand):
    answer = ''
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    left, right = '*', '#'

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        else:
            num_pos = keypad[num]
            left_pos = keypad[left]
            right_pos = keypad[right]
            left_dist = abs(num_pos[0] - left_pos[0]) + abs(num_pos[1] - left_pos[1])
            right_dist = abs(num_pos[0] - right_pos[0]) + abs(num_pos[1] - right_pos[1])
            if left_dist < right_dist:
                answer += 'L'
                left = num
            elif left_dist > right_dist:
                answer += 'R'
                right = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num

    return answer
