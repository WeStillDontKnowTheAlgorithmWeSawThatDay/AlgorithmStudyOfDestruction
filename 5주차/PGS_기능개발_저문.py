def solution(queue, speeds):
    answer = []
    while queue:
        for i in range(len(queue)):
            queue[i] += speeds[i]

        count = 0
        while queue:
            if queue[0] >= 100:
                queue.pop(0)
                speeds.pop(0)
                count += 1
            else:
                break

        if count != 0:
            answer.append(count)

    return answer