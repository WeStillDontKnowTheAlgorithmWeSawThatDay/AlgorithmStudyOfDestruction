def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        s = ''
        for i in st:
            if i in skill:
                s += i
        if skill[:len(s)] == s:
            answer += 1
    return answer
