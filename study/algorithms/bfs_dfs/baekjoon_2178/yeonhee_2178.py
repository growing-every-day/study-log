import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append((r,c))
    
    while q:
        (x,y) = q.popleft()

        if x == len(graph)-1 and y == len(graph[0])-1:
            return graph[x][y]
        
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]

            if nx not in range(0, len(graph)) or ny not in range(0, len(graph[0])):
                continue
                
            if graph[nx][ny] == 0:
                continue

            ## 핵심..!!! 
            # 1 이상이라는 건 이미 지나온 길이라는 것 
            if graph[nx][ny] > 1: 
                continue
            
            graph[nx][ny] = graph[x][y]+1
            q.append((nx,ny))
            
    return graph[len(graph)-1][len(graph[0])-1]



if "__main__" == __name__:
    n,m = map(int, input().split(" "))
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().rstrip())))

    # 동 서 남 북
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    print(bfs(0,0))
