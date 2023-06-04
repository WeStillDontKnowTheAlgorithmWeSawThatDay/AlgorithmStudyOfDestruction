import heapq

def solution(jobs):

    answer = 0
    length = len(jobs)

    heapq.heapify(jobs)
    current = 0 # 현재 시간
    work = 0 # 작업 넘버
    time = [] # 대기시간(작업을 시작한 시점 - 작업이 요청되는 시점) + 작업시간

    while work < length:
        heap = []
        for job in jobs:
            if job[0] <= current:
                heapq.heappush(heap, (current + job[1], job))

        if heap: # heap이 비어있지 않으면
            pop = heapq.heappop(heap)
            # print("pop element:", pop)
            wait_time = current - pop[1][0]
            work_time = pop[1][1]
            time.append(wait_time + work_time)
            
            jobs.remove(pop[1])
            work += 1
            current += pop[1][1]

        else: 
            # heapq.heapify(jobs)
            current = jobs[0][0]

    answer = sum(time, 0.0)/len(time)
    # print(int(answer))
    return int(answer)
    