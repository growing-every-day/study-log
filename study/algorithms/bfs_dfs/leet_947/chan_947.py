from collections import defaultdict, Counter
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dx = defaultdict(list)
        dy = defaultdict(list)
        uf = UnionFind(len(stones))

        for i, (x, y) in enumerate(stones):
            if x in dx:
                uf.union(i, dx[x][0])
            if y in dy:
                uf.union(i, dy[y][0])
            dx[x].append(i)
            dy[y].append(i)
        return sum([v-1 for k, v in Counter(uf.root).items()])