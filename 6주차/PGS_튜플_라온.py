def solution(s):
    answer = []
    s = s.lstrip("{{").rstrip("}}")
    sets = s.split("},{")
    sets.sort(key=lambda x:len(x))
    for set in sets:
        elems = set.split(",")
        for elem in elems:
            if int(elem) not in answer:
                answer.append(int(elem))
    return answer
    