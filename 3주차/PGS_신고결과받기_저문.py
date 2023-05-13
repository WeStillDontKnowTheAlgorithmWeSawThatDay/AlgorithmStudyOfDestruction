from collections import defaultdict


def solution(id_list, reports, k):
    attacked_dict, attack_dict, answer_dict = {}, defaultdict(list), {}

    for id in id_list:
        attacked_dict[id] = 0
        answer_dict[id] = 0

    reports = list(set(reports))

    for report in reports:
        temp = report.split()
        attack_dict[temp[0]].append(temp[1])
        attacked_dict[temp[1]] += 1

    black_list = []
    for key in attacked_dict:
        if attacked_dict[key] >= k:
            black_list.append(key)

    for black in black_list:
        for attacker in attack_dict:
            if black in attack_dict[attacker]:
                answer_dict[attacker] += 1

    return list(answer_dict.values())
