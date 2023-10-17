def solution(people, limit):
    answer = 0

    people.sort()
    le = 0
    ri = len(people) - 1

    while le <= ri:
        answer += 1
        if people[ri] + people[le] <= limit:
            le += 1
        ri -= 1

    return answer
