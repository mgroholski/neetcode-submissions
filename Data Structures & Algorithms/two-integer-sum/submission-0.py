class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDict = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in seenDict:
                return [seenDict[complement], i]
            seenDict[val] = i
        return -1