import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    while f_queue:
        (x, y) = f_queue.popleft()

        for i in range(4):
            dx = x + dr[i]
            dy = y + dc[i]
            if dx < 0 or dx >= R or dy <0 or dy>=C:
                continue

            if f_visited[dx][dy] != 0 or maze[dx][dy] == '#':
                continue

            f_visited[dx][dy] = f_visited[x][y] + 1
            f_queue.append((dx, dy))


    while j_queue:
        (x, y) = j_queue.popleft()
        for i in range(4):
            dx = x + dr[i]
            dy = y + dc[i]

            if dx < 0 or dx >= R or dy <0 or dy>=C:
                return j_visited[x][y]

            if j_visited[dx][dy] != 0 or maze[dx][dy] == '#' or \
                (f_visited[dx][dy] != 0 and f_visited[dx][dy] <= j_visited[x][y]+1):    # important code
                continue

            j_visited[dx][dy] = j_visited[x][y] + 1
            j_queue.append((dx, dy))

    return "IMPOSSIBLE"


if "__main__" == __name__:
    R, C = map(int, input().split(" "))
    
    # 동 서 남 북
    dr = [0, 0, 1,-1]
    dc = [1,-1, 0, 0]

    j_init_pos = None
    f_init_pos = None

    maze = [[0 for i in range(C)] for j in range(R)]

    j_queue = deque()
    f_queue = deque()

    f_visited, j_visited = [[0 for i in range(C)] for j in range(R)], [[0 for i in range(C)] for j in range(R)]    # declare fire, jihoon visited

    # 불은 여러개 일 수 있다.
    for r_idx in range(R):
        input_str = input().rstrip()
        for stri, str in enumerate(input_str):
            # 지훈이 초기 위치
            if str == "J":
                j_visited[r_idx][stri] = 1
                j_queue.append((r_idx, stri))
            # 불 초기 위치
            if str == "F":
                f_visited[r_idx][stri] = 1
                f_queue.append((r_idx, stri))    

            maze[r_idx][stri] = str
                

    print(bfs()) 
                