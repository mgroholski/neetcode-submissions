'''
Number of connected components. We could use union find to find the amount of unique parents. We could easierly look throught the edges and DFS if they haven't been seen before.

'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjDict = {i: [] for i in range(n)}
        for u,v in edges:
            adjDict[u].append(v)
            adjDict[v].append(u)

        res = 0
        seenSet = set()
        for i in range(n):
            if i not in seenSet:
                res += 1
                stack = [i]
                while stack:
                    u = stack.pop()
                    for v in adjDict[u]:
                        if v not in seenSet:
                            stack.append(v)
                            seenSet.add(v)

        return res
    

        