import sys
## 재귀 호출 최대 횟수 늘려줌
sys.setrecursionlimit(10**6)

## dfs 
def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False

# 테스트 케이스 개수
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    # 가로, 세로, 배추 개수
    M, N, K = map(int, sys.stdin.readline().rstrip().split())

    # 밭 만들기
    graph = [[0] * M for _ in range(N)]

    # 배추 심기
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[y][x] = 1

    # 배추흰지렁이 개수
    cnt = 0

    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                cnt += 1
    
    print(cnt)
