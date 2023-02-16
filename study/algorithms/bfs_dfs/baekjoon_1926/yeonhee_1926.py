import sys
from collections import deque
input = sys.stdin.readline

# 34904kb	744ms
def bfs(r,c):
    picq = deque()
    picq.append((r,c))

    pic_size = 0
    while picq:
        (x,y) = picq.popleft()
        graph[x][y] = 0
        pic_size = pic_size+1
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]

            if nx not in range(0, R) or ny not in range(0, C):
                continue

            if graph[nx][ny] == 0:
                continue

            graph[nx][ny] = 0
            picq.append((nx,ny))

    return pic_size



if "__main__" == __name__:
    R,C = map(int, input().split(" "))

    graph = [] * R
    for mi in range(R):
        graph.append(list(map(int, input().split(" "))))

    #graph = [list(map(int, input().split())) for _ in range(R)]

    # 동 서 남 북
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    result_list = []
    for r in range(R):
        for c in range(C):
            if graph[r][c] == 0:
                continue
            result_list.append(bfs(r,c))
        
    print(len(result_list))
    print(max(result_list) if len(result_list) != 0 else 0)
