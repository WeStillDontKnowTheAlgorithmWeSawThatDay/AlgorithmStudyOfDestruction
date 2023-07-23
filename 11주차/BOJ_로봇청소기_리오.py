n,m = map(int,input().split())
x,y,d = map(int,input().split())
graph = [[0]*m for _ in range(n)]
for i in range(n) :
    graph[i] = list(map(int,input().split()))

dirt = [[(0,-1),(1,0),(0,1),(-1,0)],[(-1,0),(0,-1),(1,0),(0,1)],[(0,1),(-1,0),(0,-1),(1,0)],[(1,0),(0,1),(-1,0),(0,-1)]]
ans = 0
wall = []
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            wall.append((i,j))

while True :
    if graph[x][y] == 0 :
        ans +=1
        graph[x][y] = 1

    if graph[x+dirt[d][0][0]][y+dirt[d][0][1]] == 1 and graph[x+dirt[d][1][0]][y+dirt[d][1][1]] == 1 and graph[x+dirt[d][2][0]][y+dirt[d][2][1]] == 1 and graph[x+dirt[d][3][0]][y+dirt[d][3][1]] == 1:
        a,b = dirt[d][1]
        if (x+a,y+b) in wall :
            print(ans)
            break
        else :
            x += a
            y += b
    else :
        l = dirt[d]
        for a,b in l :
            d = (d+3)%4
            if x+a>=0 and x+a<n and y+b>=0 and y+b<m :
                if graph[x+a][y+b] == 0 :
                    x += a
                    y += b
                    break
