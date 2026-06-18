import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i : set() for i in range(n)}

        for u, v, weight in flights:
            adjList[u].add((v, weight))
        
        stack = [(0, 0, src)]

        minPrice = float('inf')

        while stack:
            currentPrice, stops, u = stack.pop()

            if u == dst:
                minPrice = min(minPrice, currentPrice)

            if stops <= k:
                for v, price in adjList[u]:
                    stack.append((currentPrice + price, stops + 1, v))

        return -1 if minPrice == float('inf') else minPrice

        