class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kArr = []

        for i in nums:
            heapq.heappush(kArr, i)
            while len(kArr) > k:
                r = heapq.heappop(kArr)

        return min(kArr)
        