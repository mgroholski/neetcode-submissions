class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDict = {}

        for i, n in enumerate(nums):
            difference = target - n

            if difference in seenDict:
                return [seenDict[difference], i]

            seenDict[n] = i

        
        