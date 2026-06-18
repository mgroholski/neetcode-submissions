class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalSum = 0

        for i in nums:
            totalSum += i

        idealSum = int((len(nums) * (len(nums) + 1)) / 2)
        return idealSum - totalSum