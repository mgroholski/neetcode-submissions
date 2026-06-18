import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i : set() for i in range(n)}

        for time in times:
            u, v, weight = time
            adjList[u - 1].add((v - 1, weight))

        weights = [float('inf')] * n
        weights[k - 1] = 0

        visitedSet = set()
        
        minHeap = [(0, k - 1)]

        while minHeap:
            distance, u = heapq.heappop(minHeap)

            if u in visitedSet:
                continue

            visitedSet.add(u)
            
            for v, distance in adjList[u]:
                weights[v] = min(weights[v], weights[u] + distance)
                heapq.heappush(minHeap, (weights[v], v))

        maxWeight = max(weights)
        return -1 if maxWeight == float('inf') else maxWeight

