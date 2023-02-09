import sys, heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 거리와 도시 저장
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 다음에 가야하는 도시의 거리가 거리 정보가 저장된 리스트보다 크다면 넘기기
        if distance[now] < dist: continue

        # 현재 도시와 연결된 도시들 탐색
        for next_node in graph[now]:
            cost = dist + next_node[1]
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(q, (cost, next_node[0]))


# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호 입력
n, m, k, x = map(int, sys.stdin.readline().split())

inf = 1234567890

graph = [[] for _ in range(n + 1)]

# 거리 정보의 값으로 inf로 초기화
distance = [inf] * (n + 1)

# 각 도시 정보 입력
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))

# 다익스트라 호출
dijkstra(x)

# 거리 정보가 k와 일치하는지 확인
flag = False

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        flag = True

# flag가 False 일 경우, 거리 정보가 k와 일치하는게 없다는 의미이므로 -1 출력
if not flag:
    print(-1)

"""
    문제 : 18352번 - 특정 거리의 도시 찾기
    메모리 : 171056 KB
    시간 : 2928 ms
"""
