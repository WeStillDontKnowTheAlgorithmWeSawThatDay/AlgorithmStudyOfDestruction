def solution(jobs):
    leng = len(jobs)
    jobs.sort(key=lambda x : (x[1]))

    dq = jobs
    ans = []
    ct = 0
    while dq:
        for i in range(len(dq)):
            if dq[i][0] <= ct:
                ct += dq[i][1]
                ans.append(ct - dq[i][0])
                dq.pop(i)
                break
            if i == len(dq) - 1:
                ct += 1
    
    return sum(ans)//leng
