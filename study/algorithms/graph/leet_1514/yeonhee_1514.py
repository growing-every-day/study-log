import math
import heapq
# Runtime 875 ms Memory 28.5 MB
class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        # 출발 지점 부터 각 노드까지의 최대 거리
        distances = [ 0.0 for i in range(n)]

        # graph
        graph = dict()
        for i in range(n):
            graph[i] = list()

        for i, conn in enumerate(edges):
            graph[conn[0]].append((succProb[i], conn[1])) # (비중, 목적지인덱스)
            graph[conn[1]].append((succProb[i], conn[0])) # (비중, 목적지인덱스)

        # 자기 자신까지는 비중 0
        distances[start] = 0
        queue = []
        heapq.heappush(queue, (-distances[start], start)) # 최대 힙
        visited = [ False for i in range(n)]

        while queue:
            dist , index = heapq.heappop(queue)
            dist = -dist
            distances[index] = max(distances[index], dist)
            values = graph.get(index, None)
            if None != values:
                for v in values:
                    # v[0] : 비중, v[1] : 연결된 index

                    if visited[v[1]] == True:
                        continue
                    
                    x = distances[index] if distances[index] > 0  else 1 
                    heapq.heappush(queue, (-v[0]*x, v[1]))

            visited[index] = True

        return distances[end]

s = Solution()
print(s.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))
print(s.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))
print(s.maxProbability(3, [[0,1]], [0.5], 0, 2))
