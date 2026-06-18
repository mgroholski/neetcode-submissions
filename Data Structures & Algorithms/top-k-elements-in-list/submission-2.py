
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        for i in nums:
            if i not in freqDict:
                freqDict[i] = 0

            freqDict[i] += 1

        maxHeap = []
        for i,v in freqDict.items():
            heapq.heappush(maxHeap, (-1 * v, i))

        res = []
        while k > 0:
            _, i = heapq.heappop(maxHeap)
            res.append(i)
            k -= 1

        return res
        