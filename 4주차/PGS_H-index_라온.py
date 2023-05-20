def solution(citations):
    citations.sort()
    for i, citation in enumerate(citations[::-1]):
        if citation < i+1:
            return i
    return len(citations)
