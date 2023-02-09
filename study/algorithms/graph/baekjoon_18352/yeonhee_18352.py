import sys
import heapq
import math
input = sys.stdin.readline
# 	168488kb	1260ms

n,m,k,x = map(int, input().split(" "))
# 노드 연결 상태를 나타낼 dict
graph = dict()
for i in range(n+1):
    graph[i+1] = list()

# start에서 인덱스의 노드까지 거리
distances = [ math.inf for i in range(n+1)]
# 이미 연결상태 순회가 끝난 노드인지 여부
visited = [ False for i in range(n+1)]

for i in range(m):
    s,e = map(int, input().split(" "))
    graph[s].append(e)
    
queue = []
# 시작위치의 distance는 자기 자신까지의 거리니까 0으로 세팅하고 시작
distances[x] = 0
heapq.heappush(queue, (distances[x], x))

while queue:
    dist, idx = heapq.heappop(queue)
    if True == visited[idx]:
        continue

    distances[idx] = min(distances[idx], dist)
    values = graph.get(idx)
    # k보다 크거나 같으면 현재 노드에서 연결된 인덱스로 또 이동할 이유가 없으니까 continue
    if dist >= k:
        continue
    
    # 현재 노드에서 연결된, 이동가능한 노드들 정보 힙에 넣어준다.
    for v in values:
        heapq.heappush(queue, (dist+1, v))

    # 현재 노드 순회여부 True로 업데이트
    visited[idx] = True

if k not in distances:
    print(-1)
else:    
    for i, d in enumerate(distances):
        if d == k:
            print(i)