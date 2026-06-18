class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)

            diff = -1 * abs(a - b)

            if diff < 0:
                heapq.heappush(stones, diff)

        return 0 if not stones else -1 * stones[0]
        