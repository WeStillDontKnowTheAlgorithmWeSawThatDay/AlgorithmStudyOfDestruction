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
        if heap:
            pop = heapq.heappop(heap)
            wait_time = current - pop[1][0]
            work_time = pop[1][1]
            time.append(wait_time + work_time)
            
            jobs.remove(pop[1])
            work += 1
            current += pop[1][1]

        else: 
            current = jobs[0][0]
    return sum(time, 0.0)//len(time)
    

# 간결한 풀이
def solution(jobs): 
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, (j[1], j[0]))
        
        if heap:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
        else:
            now += 1
    return answer // i