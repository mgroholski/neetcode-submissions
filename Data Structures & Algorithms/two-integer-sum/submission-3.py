class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxDict = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in idxDict:
                return [idxDict[diff], idx]
            idxDict[num] = idx

        return -1
        