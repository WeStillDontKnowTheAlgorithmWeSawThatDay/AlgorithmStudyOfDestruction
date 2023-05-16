def solution(id_list, report, k):
    reportee = {user:0 for user in id_list} # 신고 당한 사람
    reporter = {user:0 for user in id_list} # 신고한 사람
    for row in set(report):
        user, bad_user = row.split(" ")
        reportee[bad_user] += 1
            
    for row in set(report):
        user, bad_user = row.split(" ")
        if reportee[bad_user] >= k:
            reporter[user] += 1

    return [num for num in reporter.values()]
