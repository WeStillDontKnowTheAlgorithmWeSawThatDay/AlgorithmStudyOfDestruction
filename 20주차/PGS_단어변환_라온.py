from collections import deque

def compare(word, target):
    flag = 0
    for i in range(len(target)):
        if word[i] != target[i]:
            flag += 1
    return flag == 1

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    queue = deque()
    queue.append([begin, 0])
    
    while queue:
        word, depth = queue.popleft()
        if word == target:
            return depth
        
        for i in range(len(words)):
            if compare(word, words[i]):
                queue.append([words[i], depth + 1])
    return answer
