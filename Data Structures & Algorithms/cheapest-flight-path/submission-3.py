'''
We are searching for the cheapest path from src to dst. We can use Dijkstra's algorithm to create a MST. Then, DFS.

However, we can also use priority search. The first path to reach sink with sufficent stops is the cheapest (given there's no negative edges).

'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjDict = {i: [] for i in range(n)}
        for u,v,w in flights:
            adjDict[u].append((v,w))

        minHeap = [(0, 0, src)]
        while minHeap:
            w, stops, u = heapq.heappop(minHeap)

            if u == dst and stops - 1 <= k:
                return w
            elif stops - 1 > k:
                continue

            for v,p in adjDict[u]:
                heapq.heappush(minHeap, (w + p, stops + 1, v))

        return -1