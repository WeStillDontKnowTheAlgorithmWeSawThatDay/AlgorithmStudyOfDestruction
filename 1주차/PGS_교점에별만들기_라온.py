## 최소, 최대 x y 구하는 로직에서 주석처럼 하면 시간초과남 ;

def solution(lines):
    answer = []      
    dots = []
    
    for i in range(len(lines)):
        for line in lines[i+1:]:
            
            a, b, e = lines[i]
            c, d, f = line
            
            x_up = b*f - e*d
            y_up = e*c - a*f
            xy_under = a*d - b*c
            
            if xy_under != 0:
                x = x_up / xy_under
                y = y_up / xy_under
                
                if isInts(x, y):
                    dots.append((int(x),int(y)))

    min_x = 1000
    min_y = 1000
    max_x = -1000
    max_y = -1000

    dots = list(set(dots))
    
    x_dot_list = [dot[0] for dot in dots]
    y_dot_list = [dot[1] for dot in dots]
    min_x, max_x = min(x_dot_list), max(x_dot_list)
    min_y, max_y = min(y_dot_list), max(y_dot_list)
    
    # for x, y in dots:
    #     min_x = min(x, min_x)
    #     min_y = min(y, min_y)
    #     max_x = max(x, max_x)
    #     max_y = max(y, max_y)
    
    x_range = max_x - min_x + 1
    y_range = max_y - min_y + 1

    graph = [["." for _ in range(min_x, max_x+1)] for _ in range(max_y, min_y-1,-1)]
    
    for x, y in dots:
        graph[abs(y - min_y)][abs(x - min_x)] = "*"
    
    for g in graph:
        answer.append("".join(g))
    return answer[::-1]

def isInts(a, b):
    return int(a) == a and int(b) == b
        