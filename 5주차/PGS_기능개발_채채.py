def solution(progresses, speeds):
    answer = []
    while progresses :
        cnt = 0
        while progresses and progresses[0] >= 100:
            cnt+=1
            progresses.pop(0)
            speeds.pop(0)

        progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]
        if cnt:
            answer.append(cnt)
    
    return answer
