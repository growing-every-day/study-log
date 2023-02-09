import math
import heapq

#  387 ms, 15.8 MB
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        min_times = [6000 for i in range(n+1)]
        visited = [False for i in range(n+1)]
        queue = []
        min_times[k] = 0
        min_times[0] = 0 # 안쓰는거 채워줌
        heapq.heappush(queue, (min_times[k], k))

        # 연결상태 나타내는 dict만들기
        graph = dict()
        for i in range(n+1):
            graph[i] = list()

        for time in times:
            graph[time[0]].append((time[2], time[1])) #(비중, 인덱스)으로 저장

        while queue:
            dist, idx = heapq.heappop(queue)
            if visited[idx] == True:
                continue

            values = graph.get(idx, None)
            if values == None:
                continue
            
            for v in values:
                # 경로가 현재 저장된 것 보다 더 길어지면 heapq에 넣어줄 이유가 없음
                if min_times[v[1]] < min_times[idx] + v[0]:
                    continue
                min_times[v[1]] = min_times[idx] + v[0]
                heapq.heappush(queue, (min_times[v[1]], v[1]))

            visited[idx] = True

        if 6000 in min_times:
            return -1

        return max(min_times)


s = Solution()
print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))

print(s.networkDelayTime([[1,2,1]], 2, 1))

print(s.networkDelayTime([[1,2,1]], 2, 2))

print(s.networkDelayTime([[1,2,1],[2,1,3]], 2, 2))