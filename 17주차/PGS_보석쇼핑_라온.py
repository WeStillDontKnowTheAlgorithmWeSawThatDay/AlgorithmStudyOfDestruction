# ***, 너무 어렵다 ? 
def solution(gems):
    answer = [0, len(gems)]
    gem_set = set(gems)
    kind = len(gem_set)
    start, end = 0, 0    
    visited_dict = {gems[0]: 1}
    
    while start <= end:
        visited_num = len(visited_dict.keys())
        if visited_num < kind:
            end += 1
            if end >= len(gems):    break
            if visited_dict.get(gems[end]) == None:
                visited_dict[gems[end]] = 1
            else:
                visited_dict[gems[end]] += 1
            
        elif visited_num == kind:
            if end - start < answer[1] - answer[0]:
                answer = [start+1, end+1]
            
            visited_dict[gems[start]] -= 1
            if visited_dict[gems[start]] == 0:
                del visited_dict[gems[start]]
            start += 1
    return answer

''' 외않되
import sys
def solution(gems):
    gem_set = set(gems)
    gem_dict = {}
    
    for i, gem in enumerate(gem_set):
        gem_dict[gem] = i
    
    start, end = 0, 0
    visited = [False for _ in gems]  
    visited_num = 0
    expected_idx = {}
    mmin = sys.maxsize
    
    for i, gem in enumerate(gems):
        idx = gem_dict[gem]
        if visited[idx] and gem == gems[start]: # 이미 방문했으면
            start += 1
            while start < len(gems) - 1:
                if gems[start] == gems[start+1]:
                    start += 1
                else:
                    break
        elif not visited[idx]: # 방문한적 없으면
            visited_num += 1
            visited[idx] = True
        print(gem, start, end, visited_num)
        if visited_num == len(gem_set) and 0 <= i - start < mmin:
            end = i
            mmin = end - start
            print(mmin)
            # break
            
    answer = [start+1, end+1]
    return answer

'''