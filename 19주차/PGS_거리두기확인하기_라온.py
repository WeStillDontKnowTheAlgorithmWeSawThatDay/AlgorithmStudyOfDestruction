def check(place, i, j):
    # diagnoal
    if i <= 3 and j <= 3: # right-down diagnoal
        d, r, diag = place[i+1][j], place[i][j+1], place[i+1][j+1]
        if diag == 'P' and (r != 'X' or d != 'X'):
            return True
    if i <= 3 and j >= 1: # left-down diagonal
        d, r, diag = place[i+1][j], place[i][j-1], place[i+1][j-1]
        if diag == 'P' and (r != 'X' or d != 'X'):
            return True
        
    # rr, dd, r, d
    if i + 2 <= 4 and j + 2 <= 4:
        d, dd = place[i+1][j], place[i+2][j]
        r, rr = place[i][j+1], place[i][j+2]
        if d == 'P' or r == 'P':
            return True
        if (dd == 'P' and d != 'X') or (rr == 'P' and r != 'X'):
            return True
    
    if i >= 3:
        if i == 3:
            d = place[i+1][j]
            if d == 'P':
                return True

        if j + 2 <= 4: # 0, 1, 2
            r, rr = place[i][j+1], place[i][j+2]
            if r == 'P' or (rr == 'P' and r != 'X'):
                return True
    
        if j + 1 == 4: # 3
            r = place[i][j+1]
            if r == 'P':
                return True

    if j >= 3:
        if j == 3:
            r = place[i][j+1]
            if r == 'P':
                return True
            
        if i + 2 <= 4:
            d, dd = place[i+1][j], place[i+2][j]
            if d == 'P' or (dd == 'P' and d != 'X'):
                return True
    
        if i + 1 == 4:
            d = place[i+1][j]
            if d == 'P':
                return True
    return False

def solution(places):
    answer = [1, 1, 1, 1, 1]
    for n, place in enumerate(places):
        for i in range(0, 5):
            for j in range(0, 5):
                if place[i][j] == 'P' and check(place, i, j):
                    answer[n] = 0
                    break
            if answer[n] == 0:
                break
    return answer