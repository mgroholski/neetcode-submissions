'''
A tree is valid if it is
1. Connected 
2. No cycles

Do with disjoint set unions!!! 

'''


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjDict = {i: [] for i in range(n)}
        for u,v in edges:
            adjDict[u].append(v)
            adjDict[v].append(u)
        

        seenSet = set()
        stack = [(0, -1)]

        while stack:
            u, par = stack.pop()

            if u in seenSet:
                return False
            
            seenSet.add(u)
            for v in adjDict[u]:
                if v != par:
                    stack.append((v, u))

        return len(seenSet) == n



        