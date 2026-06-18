class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def find(self, p):
        if p == self.parents[p]:
            return p

        return self.find(self.parents[p])

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)

        if self.rank[pRoot] > self.rank[qRoot]:
            self.parents[qRoot] = pRoot
        elif self.rank[pRoot] < self.rank[qRoot]:
            self.parents[pRoot] = qRoot
        else:
            self.parents[qRoot] = pRoot
            self.rank[pRoot] += 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionFind = UnionFind(len(edges))

        for edge in edges:
            u,v = edge
            if unionFind.connected(u - 1,v - 1):
                return edge
            else:
                unionFind.union(u - 1, v - 1)




        