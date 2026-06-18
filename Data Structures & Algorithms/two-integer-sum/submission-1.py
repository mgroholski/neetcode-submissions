class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDict = {}

        for idx, i in enumerate(nums):
            d = target - i
            if d in seenDict:
                return [seenDict[d], idx]
            
            seenDict[i] = idx

        return -1

        