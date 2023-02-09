import sys, heapq

# 다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next_node in graph[node]:
            if dist+next_node[1] < distance[next_node[0]]:
                distance[next_node[0]] = dist + next_node[1]
                heapq.heappush(q, (dist+next_node[1], next_node[0]))


# 정점의 개수와 간선의 개수 입력
n, m = map(int, sys.stdin.readline().split())

# 시작 정점의 번호
k = int(sys.stdin.readline())

graph = [ [] for _ in range(n+1)]

# 간선 정보 입력
for _ in range(m):
    # u에서 v로 가는 가중치 w인 간선
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

# 거리 정보 inf로 초기화
inf = 1234567890
distance = [inf] * (n+1)
distance[k] = 0

dijkstra(k)

for i in range(1, n+1):
    if distance[i]==inf:
        print('INF')
    else:
        print(distance[i])

"""
    문제 : 1753번 - 최단경로
    메모리 : 67256 KB
    시간 : 668 ms
"""
