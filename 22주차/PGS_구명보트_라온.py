# **, 이것도 못푸냐 !! 
def solution(people, limit):
    answer = 0
    left, right = 0, len(people) - 1
    people.sort(reverse = True)
    while True:
        if people[left] + people[right] > limit:
            answer += 1
            left += 1
        else:
            answer += 1
            left += 1
            right -= 1
        if left > right:
            break
    return answer
