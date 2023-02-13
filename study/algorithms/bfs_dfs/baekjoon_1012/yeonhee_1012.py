import sys
from collections import deque 
input = sys.stdin.readline

# 34200kb	76ms
def bfs(rowIdx, colIdx ):
    q = deque()
    q.append((rowIdx, colIdx))
    while q:
        r, c = q.popleft()
        visited[r][c] = True
        for i in range(4):
            _dc = c + dc[i]
            _dr = r + dr[i]

            if _dr >= n or _dr < 0 or _dc >= m or _dc < 0 or ground[_dr][_dc] == 0:
                continue

            ground[_dr][_dc] = 0

            q.append((_dr, _dc))




if __name__== "__main__":
    testcase = int(input())

    for _ in range(testcase):
        # m :  col, n : row
        m,n,k = map(int, input().split(" "))
        ground = [[0 for i in range(m)] for j in range(n)]
        visited = [[False for i in range(m)] for j in range(n)]

        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        
        for _ in range(k):
            _c ,_r = map(int, input().split(" "))
            ground[_r][_c] = 1

        result = 0
        for rowIdx in range(n):
            for colIdx in range(m):
                if ground[rowIdx][colIdx] == 0:
                    continue

                ground[rowIdx][colIdx] = 0
                bfs(rowIdx, colIdx)
                result = result+1

        print(result)