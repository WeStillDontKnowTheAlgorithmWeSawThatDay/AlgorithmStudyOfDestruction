# *, distance 구하는법
from collections import deque

def solution(n, vertex):
    answer = 0
    visited = {}
    graph = {i:[] for i in range(1, n+1)}
    for i in range(1, len(graph)+1):
        visited[i] = False

    for src, dst in vertex:
        graph[src].append(dst)
        graph[dst].append(src)

    distance = [0]*(n+1)
    queue = deque([1])    
    visited[1] = True
    while queue:
        flag = False
        now = queue.popleft()
        line = graph[now]
        for i in line:
            if visited.get(i) == False:
                queue.append(i)
                visited[i] = True   
                distance[i] = distance[now] + 1
    
    mmax = max(distance)
    for d in distance:
        if d == mmax:
            answer += 1
    return answer


'''
from collections import deque
def solution(n, edge):
    
    length = [-1]*n # 노드 1로부터의 길이
    check = [0]*n # 방문했는지 체크 
    depth = 0
    
    vtx = 1 # 시작노드
    length[0] = 0 # 노드1은 길이 0

    queue = deque() # BFS를 큐로 구현

     # 1: [[1,2], [1,3]] <- 해당 노드랑 인접한 엣지들을 딕셔너리 형태로
    temp = { i+1 : deque() for i in range(n) }
    for e in edge:
        temp[e[0]].append(e)
        temp[e[1]].append(e)

    while True:
        check[vtx-1] = 1   
        
        depth = length[vtx-1] + 1
        
        for e in temp[vtx]:
            if check[e[0]-1] == 1 and check[e[1]-1] == 1: continue # [1,2] : 1,2 둘다 방문한 노드면 아래 코드 실행 ㄴ    
            
            queue.append(e)

            # 현재 탐색하고 있 노드와 인접한 노드 찾기 ([1,2] <- 이런 형태이므로 1이 탐색하고 있는 노드라면 2를 찾아야함 즉, vtx가 아닌 노드 찾기)
            if e[0] == vtx: i = e[1] 
            else:   i = e[0]

            if length[i-1] == -1 or depth <= length[i-1]: # -1(방문한 적 없음)이거나 현재 거리가 depth보다 크면 업데이트
                length[i-1] = depth

        if not queue:   break # 무한루프 탈출
        
        while queue: # 큐가 비거나 방문 안한 노드가 나올 때까지 무한 pop
            pop = queue.popleft()  # 큐 왼쪽 끝부터 pop
            
            if check[pop[0]-1] == 0: # pop[0] 방문안한 노드
                temp[pop[1]].remove(pop)
                vtx = pop[0] # 방문 안한 노드를 vtx로 만들어줌
                break 
                
            if check[pop[1]-1] == 0: # pop[1] 방문안한 노드
                temp[pop[0]].remove(pop)
                vtx = pop[1] # 방문 안한 노드를 vtx로 만들어줌
                break

    return length.count(max(length))

'''