from collections import deque
import sys

# 48408 KB	1372 ms
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())

board = []
jihoon = deque()
fire = deque()

for i in range(N):
    board.append(list(input().strip()))
    for j in range(M):
        if board[i][j] == 'J':
            jihoon.append((i, j))
            board[i][j] = 1
        if board[i][j] == 'F':
            fire.append((i, j))

def move_jihoon():
    length = len(jihoon)
    for _ in range(length):
        x, y = jihoon.pop()
        if board[x][y] != 'F':
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if board[nx][ny] != '#' and board[nx][ny] != 'F' and not visited[nx][ny]:
                        board[nx][ny] = board[x][y] + 1
                        visited[nx][ny] = True
                        jihoon.appendleft((nx, ny))
                else:
                    return board[x][y]

def move_fire():
    length = len(fire)
    for _ in range(length):
        x, y = fire.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] != '#' and board[nx][ny] != 'F':
                    board[nx][ny] = 'F'
                    fire.appendleft((nx, ny))

min_time = 0
visited = [[False] * M for _ in range(N)]
visited[jihoon[0][0]][jihoon[0][1]] = True

while True:
    min_time = move_jihoon()
    if min_time or not jihoon:
        break
    move_fire()

if not min_time:
    print('IMPOSSIBLE')
else:
    print(min_time)
