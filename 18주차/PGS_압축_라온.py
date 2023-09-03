def solution(msg):
    answer = []
    index = {chr(64 + i):i for i in range(1, 27)}
    idx, length = 0, 0
    num = 27
    
    while idx + length < len(msg):
        w = msg[idx:idx+length+1]
        length += 1
        wc = msg[idx:idx+length+1]
        while index.get(wc) is not None and idx+length < len(msg):
            length += 1
            wc = msg[idx:idx+length+1]
        
        if index.get(wc) is None:
            w = msg[idx:idx+length]
            answer.append(index[w])
            index[wc] = num
        else:
            answer.append(index[wc])
        idx = idx + length
        num += 1
        length = 0
    return answer
