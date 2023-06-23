def solution(begin, target, words):
    if target not in words:
        return 0
    checked = dict()
    for word in words:
        checked[word] = 0
        
    b = []
    b.append(begin)
    
    count = 0
    while b:
        now = b.pop()
        if now == target:
            return count
        for word in words:
            cnt = 0
            if checked[word] == 0:
                for i in range(len(word)):
                    if now[i] == word[i]:
                        cnt += 1
                if cnt == 2:
                    count += 1
                    checked[word] = 1
                    b.append(word)
                    if word == target:
                        return count
    
    return 0
# 60점 나오는데 이유를 모르겠어요
