'''
We only can't take a course if there's a cycle within the graph. Thus, we need to check if there's a valid topo ordering.

'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        outAdj = {i:set() for i in range(numCourses)}
        inAdj = {i:set() for i in range(numCourses)}
        L = []
        S = set([i for i in range(numCourses)])
        for u,v in prerequisites:
            outAdj[u].add(v)
            inAdj[v].add(u)
            if v in S:
                S.remove(v)

        S = list(S)
        while S:
            u = S.pop(0)
            L.append(u)

            for v in outAdj[u]:
                inAdj[v].remove(u)
                if not len(inAdj[v]):
                    S.append(v)

        return len(L) == numCourses
