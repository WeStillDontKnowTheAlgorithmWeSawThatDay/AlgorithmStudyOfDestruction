def solution(name):
    count = 0
    size = len(name)
    min_move = size - 1
    
    for idx, char in enumerate(name):
        count += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next_idx = idx + 1
        while next_idx < size and name[next_idx] == 'A':
            next_idx += 1
        
        min_move = min([min_move, 2 * idx + size - next_idx, idx + 2 * (size - next_idx)])
        
    count += min_move
    return count
