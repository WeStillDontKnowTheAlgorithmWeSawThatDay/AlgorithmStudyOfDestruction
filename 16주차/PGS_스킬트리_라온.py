import sys
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        num = -1
        flag = True
        for sk in skill_tree:
            if sk in skill:
                if skill.index(sk) - 1 != num:
                    flag = False
                    break
                else:
                    num = skill.index(sk)
        if flag:
            answer += 1
    return answer
