import heapq

class UnionFind:
    def __init__(self, elements):
        self.parent = {tuple(i) : tuple(i) for i in elements}
        self.rank = {tuple(i) : 1 for i in elements}

    def find(self, p):
        p = tuple(p)

        if p == self.parent[p]:
            return p
        
        return self.find(self.parent[p])

    def union(self, p, q):
        p = tuple(p)
        q = tuple(q)

        pRoot = self.find(p)
        qRoot = self.find(q)

        if pRoot != qRoot:
            if self.rank[pRoot] > self.rank[qRoot]:
                self.parent[qRoot] = pRoot
            elif self.rank[pRoot] < self.rank[qRoot]:
                self.parent[pRoot] = qRoot
            else:
                self.parent[qRoot] = pRoot
                self.rank[pRoot] += 1

    def connected(self, p, q):
        p = tuple(p)
        q = tuple(q)
        return self.find(p) == self.find(q)
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0

        minHeap = []
        
        for i, point1 in enumerate(points):
            for j, point2 in enumerate(points[i + 1:]):
                distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                heapq.heappush(minHeap,(distance, tuple(point1), tuple(point2)))
        
    
        unionFind = UnionFind(points)
        cost = 0

        while len(minHeap):
            distance, point1, point2 = heapq.heappop(minHeap)

            if not unionFind.connected(point1, point2):
                unionFind.union(point1, point2)
                cost += distance

        return cost



        