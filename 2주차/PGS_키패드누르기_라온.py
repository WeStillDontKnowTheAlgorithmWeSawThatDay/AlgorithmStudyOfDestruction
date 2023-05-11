def solution(numbers, hand):
    answer = ''
    left, right = 10, 12
    
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            left = number
            answer += 'L'
        elif number == 3 or number == 6 or number == 9:
            right = number
            answer += 'R'
        else:
            left_cal = func(number, left)
            right_cal = func(number, right)
            if left_cal < right_cal:
                answer += 'L'
                left = number
            elif left_cal > right_cal:
                answer += 'R'
                right = number
            else:
                answer += hand[0].upper()
                if hand == 'left':  left = number
                elif hand == 'right':   right = number
    
    return answer

def func(number, hand):
    if hand == 0:   hand = 11
    if number == 0: number = 11
    if hand % 3 == 2 and number % 3 == 2:
        return abs(cal(hand) - cal(number))
    return abs(cal(hand) - cal(number)) + 1

def cal(num):
    return abs((num-1)//3)