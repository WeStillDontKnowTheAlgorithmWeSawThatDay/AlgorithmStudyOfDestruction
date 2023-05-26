def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)

    h_index = 0
    for i in range(n):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break

    return h_index
