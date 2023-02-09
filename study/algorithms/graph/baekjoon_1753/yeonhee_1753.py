import sys
import heapq
import math
input = sys.stdin.readline
# 166280kb,	660ms
v, e = map(int, input().split(" "))
s = int(input())

graph = dict()
for i in range(v+1):
    graph[i] = list()

distance = [math.inf for i in range(v+1)]
visited = [False for i in range(v+1)]

for _ in range(e):
    from_v, to_v, value = map(int, input().split(" "))
    graph[from_v].append(( value, to_v)) #(인덱스, 비중)으로 저장

queue = []
distance[s] = 0
heapq.heappush(queue, (distance[s], s))

while queue:
    dist, idx = heapq.heappop(queue)
    if visited[idx] == True:
        continue

    values = graph.get(idx, None)
    if values == None:
        continue
    
    for v in values:
        # 경로가 현재 저장된 것 보다 더 길어지면 heapq에 넣어줄 이유가 없음
        if distance[v[1]] < distance[idx] + v[0]:
            continue
        distance[v[1]] = distance[idx] + v[0]
        heapq.heappush(queue, (distance[v[1]], v[1]))

    visited[idx] = True

distance = distance[1:]
for d in distance:
    if d == math.inf:
        print("INF")
    else:
        print(d)


