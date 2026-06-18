import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            newWeight = min(s2, s1) - max(s2, s1)
            if newWeight != 0:
                heapq.heappush(stones, newWeight)

        return -stones[0] if len(stones) else 0