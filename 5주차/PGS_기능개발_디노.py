from collections import deque
import copy

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    day = 0
    while progresses:
        day += 1
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        for p in progresses:
            if p >= 100:
                cnt += 1
                p2 = copy.deepcopy(progresses)
                p2.popleft()
                # progresses.popleft()
                progresses = p2
                s2 = copy.deepcopy(speeds)
                s2.popleft()
                speeds = s2
                # speeds.popleft()
            else:
                break
        if cnt != 0:
            answer.append(cnt)
    return answer