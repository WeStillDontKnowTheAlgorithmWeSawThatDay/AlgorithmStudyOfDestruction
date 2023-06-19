import heapq

def solution(jobs):
    answer = 0
    start_time = 0  # 작업이 시작되는 시간
    current_time = 0  # 현재 시간
    heap = []  # 작업 대기열을 저장할 힙

    # 요청 시간을 기준으로 작업 리스트를 정렬
    jobs.sort(key=lambda x: x[0])

    while len(jobs) > 0 or len(heap) > 0:
        # 대기 중인 작업이 없는 경우 현재 시간을 해당 작업의 요청 시간으로 이동
        if len(heap) == 0:
            current_time = jobs[0][0]

        # 현재 시간 이전에 요청된 작업을 모두 힙에 추가
        while len(jobs) > 0 and jobs[0][0] <= current_time:
            request_time, duration = jobs.pop(0)
            heapq.heappush(heap, (duration, request_time))

        # 힙에서 가장 작업 시간이 짧은 작업을 선택하여 실행
        duration, request_time = heapq.heappop(heap)
        start_time = max(current_time, request_time)  # 작업 시작 시간
        current_time = start_time + duration  # 작업 종료 시간
        answer += (current_time - request_time)  # 작업 소요 시간 누적

    return answer // len(jobs)
