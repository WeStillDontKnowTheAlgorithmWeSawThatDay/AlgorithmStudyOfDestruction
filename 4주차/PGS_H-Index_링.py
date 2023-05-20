def solution(citations):
    citations.sort()
    citations.reverse()

    answer = 0
    if min(citations) > len(citations) :
        return len(citations)
    for i in range(len(citations)) :
        if i >= citations[i] :
            answer = i
            break

    return answer
