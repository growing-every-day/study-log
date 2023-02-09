import collections
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)

        for (s, e), p in zip(edges, succProb):
            graph[s].append((e, p))
            graph[e].append((s, p))

        probs = {i: 0 for i in range(n)}

        pq = [(-1, start)]

        while pq:
            prob, node = heapq.heappop(pq)

            for neighbor, next_prob in graph[node]:
                new_prob = prob * next_prob

                if new_prob < probs[neighbor]:
                    probs[neighbor] = new_prob
                    heapq.heappush(pq, (new_prob, neighbor))

        return -probs[end]


solution = Solution()
print(solution.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))