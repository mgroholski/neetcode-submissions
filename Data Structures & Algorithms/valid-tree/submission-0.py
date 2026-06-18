# Tree properties:
# Can reach any node from any other node
# No cycle (does not matter in this case)


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: set() for i in range(n)}
        
        for u,v in edges:
            adjList[u].add(v)
            adjList[v].add(u)


        visitedSet = set([0])
        stack = [(0, None)]


        while len(stack):
            u, addedNode = stack.pop()

            for v in adjList[u]:
                if v not in visitedSet:
                    stack.append((v,u))
                    visitedSet.add(v)
                elif v in visitedSet and v != addedNode:
                    return False

        return len(visitedSet) == n


        