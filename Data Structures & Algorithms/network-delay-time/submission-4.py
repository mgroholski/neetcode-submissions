'''
Minimum spanning tree with weighted edges.


'''


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjDict = {i:[] for i in range(n)}
        for u,v,t in times:
            adjDict[u - 1].append((v - 1,t))
        
        dist = [-1 for _ in range(n)]
        queue = [(0,k - 1)]
        visitCnt = 0

        while queue:
            t, u = heapq.heappop(queue)

            if dist[u] == -1:
                dist[u] = t
                visitCnt += 1

                for v, dt in adjDict[u]:
                    if dist[v] == -1:
                        heapq.heappush(queue, (t + dt, v))

        return max(dist) if visitCnt == n else -1
        






        