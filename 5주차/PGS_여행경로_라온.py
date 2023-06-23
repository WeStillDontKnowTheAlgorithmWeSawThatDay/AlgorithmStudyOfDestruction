def solution(tickets):
    answer = []
    
    paths = {}
    for src, dst in tickets:
        paths.setdefault(src, [])
        paths.setdefault(dst, [])
        paths[src].append(dst)
    
    for src in paths.keys():
        paths[src].sort(reverse=True)
        
    stack = ["ICN"]
    while stack:
        top = stack.pop()
        if top not in paths or not paths[top]:
            answer.append(top)
        else:
            stack.append(top)
            stack.append(paths[top].pop())
    return answer[::-1]