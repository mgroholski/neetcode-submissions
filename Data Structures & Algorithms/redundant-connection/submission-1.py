'''
We need to determine if the two are disjoint sets. Meaning we can use algorithm

'''

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i

        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_j] > self.rank[root_i]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
        

    def connected(self, i,j):
        return self.find(i) == self.find(j)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodeSet = set()
        for i,j in edges:
            nodeSet.add(i)
            nodeSet.add(j)

        f = UnionFind(len(nodeSet))

        for i,j in edges:
            i -= 1
            j -= 1
            if not f.connected(i,j):
                f.union(i,j)
            else:
                return [i+1,j+1]

        

        
        