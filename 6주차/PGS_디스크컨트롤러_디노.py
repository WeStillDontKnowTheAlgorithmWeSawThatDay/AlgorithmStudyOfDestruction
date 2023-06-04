def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: x[1])
    # print(jobs)
    now = 0
    jobs_len = len(jobs)

    while (jobs):
        for i in range(0, len(jobs)):
            if jobs[i][0] <= now:
                # print(jobs[i])
                now += jobs[i][1]
                answer += (now - jobs[i][0])
                jobs.remove(jobs[i])
                # print(now)
                break

            if i == len(jobs) - 1:
                now += 1

    return answer // jobs_len