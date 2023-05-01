def collatz(num):
    if num%2==0:
        num /= 2
    else:
        num = num*3 +1
    return num

def solution(num):
    answer = 0
    while True:
        if num == 1:
            break
        if answer > 500:
            return -1
        num = collatz(num)
        answer+=1
    return answer
