import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    scores = [0] * (N + 1)
    for _ in range(N):
        x, y = map(int, input().split())
        scores[x] = y # 서류 심사 점수별 초기화
    
    max_count = 1 # 서류 심사 1등은 항상 합격 (다른 지원자 보다 떨어지지 않기 때문에)
    max_interview_score = scores[1] # 서류 심사 1등의 면접 점수가 초기 기준 (이것 보다 잘하면 합격)

    for i in range(2, N + 1):
        # 지금까지 면접 최고 점수보다 높을 경우, 합격자 수가 늘어나고, 면접 최고 점수가 갱신된다.
        if scores[i] < max_interview_score:
            max_count += 1
            max_interview_score = scores[i]

    print(max_count)

# for _ in range(int(input())): 
#     N = int(input())
#     scores = [list(map(int, input().split())) for _ in range(N)]
#     scores.sort() # 서류 심사 점수별 정렬

#     max_count = 1 # 서류 심사 1등은 항상 합격 (다른 지원자 보다 떨어지지 않기 때문에)
#     max_interview_score = scores[0][1] # 서류 심사 1등의 면접 점수가 초기 기준 (이것 보다 잘하면 합격)

#     for i in range(1, N):
#         # 지금까지 면접 최고 점수보다 높을 경우, 합격자 수가 늘어나고, 면접 최고 점수가 갱신된다. 
#         if scores[i][1] < max_interview_score:
#             max_count += 1
#             max_interview_score = scores[i][1]
#     print(max_count)
