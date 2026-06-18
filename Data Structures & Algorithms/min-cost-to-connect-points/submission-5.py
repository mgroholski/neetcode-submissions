class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        minHeap = [(0,0)]
        
        res = 0
        nodeSeen = [False] * n
        edgesSeen = 0

        while edgesSeen < n:
            dist, u = heapq.heappop(minHeap)

            if not nodeSeen[u]:
                nodeSeen[u] = True
                res += dist

                edgesSeen += 1

                u_x, u_y = points[u]
                for v in range(len(points)):
                    if not nodeSeen[v]:
                        v_x, v_y = points[v]
                        dist = abs(u_x - v_x) + abs(u_y - v_y)
                        heapq.heappush(minHeap, (dist, v))

        return res







