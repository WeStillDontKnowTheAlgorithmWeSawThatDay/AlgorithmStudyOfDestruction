def solution(citations):
    answer = len(citations)
    citations.sort(reverse=True)

    for i in range(len(citations)):
        h = citations[i]
        if i >= h:
            return i
    return answer


# def solution(citations):
#     answer = 0
#     citations.sort()
#
#     for i in range(len(citations)):
#         h = citations[i]
#         if h >= len(citations) - i:
#             answer += 1
#
#     return answer
