def solution(tickets):
    answer = []
    
    paths = {}
    for src, dst in tickets:
        paths.setdefault(src, [])
        paths.setdefault(dst, [])
        paths[src].append(dst)
        paths[src].sort()
    print(paths)
    
    dst = 'ICN'
    answer.append(dst)
    while True:
        if len(paths[dst]) == 0:
            count = 0
            for value in paths.values():
                count += len(value)
            if count == 0:
                break
        next = paths[dst][0]
        answer.append(next)
        paths[dst].remove(next)
        dst = next
    return answer

def solution(tickets):
    answer = []
    
    paths = {}
    for src, dst in tickets:
        paths.setdefault(src, [])
        paths.setdefault(dst, [])
        paths[src].append(dst)
        paths[src].sort()
    print(paths)
    
    dst = 'ICN'
    answer.append(dst)
    # while True:
    #     if len(paths[dst]) == 0:
    #         count = 0
    #         for value in paths.values():
    #             count += len(value)
    #         if count == 0:
    #             break
        # next = paths[dst][0]
        # answer.append(next)
        # paths[dst].remove(next)
        # dst = next
    next = paths[dst][0]
    answer = find(paths, next, answer)
    return answer

def find(paths, dst, answer):
    possible = paths[dst]
    if len(possible) == 0:
        count = 0
        for value in paths.values():
            count += len(value)
        if count == 0:
            return answer
    elif len(possible) == 1:
        next = paths[dst][0]
        answer.append(next)
        paths[dst].remove(next)
        find(paths, next, answer)
    else:
        for i in range(len(possible)):
            next = paths[dst][i]
            answer.append(next)
            paths[dst].remove(next)
            find(paths, next, answer)
        