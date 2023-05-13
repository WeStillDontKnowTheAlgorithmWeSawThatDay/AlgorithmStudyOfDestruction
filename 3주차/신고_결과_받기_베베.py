def solution(id_list: list, report: list, k: int):
    unique_report = list(set(report))

    # 유저별 신고한 아이디
    reporting_user_list = {}

    # 유져별 신고 당한 횟수
    reported_user_list = {}

    for id in id_list:
        reporting_user_list[id] = []

    for id in id_list:
        reported_user_list[id] = 0

    for user_report_info in unique_report:
        infos = user_report_info.split()
        reporting_user = infos[0]
        reported_user = infos[1]

        reporting_user_list[reporting_user].append(reported_user)
        reported_user_list[reported_user] += 1

    answer = []
    for i in id_list:
        result = 0
        for u in reporting_user_list[i]:
            if reported_user_list[u] >= k:
                result += 1
        answer.append(result)
    return answer