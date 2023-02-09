import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        inf = 1234567890
        distance = [inf] * (n+1)
        distance[k] = 0

        graph = [[] for _ in range(n+1)]
        for u, v, w in times:
            graph[u].append((v, w))

        q = []
        heapq.heappush(q, (0, k))

        while q:
            dist, node = heapq.heappop(q)

            # 다음에 가야하는 노드의 거리가 거리 정보가 저장된 distance[node]보다 크다면 넘기기
            if distance[node] < dist: 
                continue

            # 인접 노드 탐색
            for next_node in graph[node]:
                # distance 리스트에 저장된 값보다 현재 노드를 거쳐간 거리가 작다면
                if dist + next_node[1] < distance[next_node[0]]:
                    # 거리 정보 갱신
                    distance[next_node[0]] = dist + next_node[1] 
                    heapq.heappush(q, (dist + next_node[1], next_node[0]))


        answer = 0

        for i in range(1, n+1):
            if answer < distance[i]:
                answer = distance[i]
        
        if answer == inf:
            answer = -1

        return answer         
 # Runtime : 372 ms, Memory : 16 MB
