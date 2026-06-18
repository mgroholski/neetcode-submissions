'''
 nums = [2,3,2,3,2]

We can follow a similiar pattern as house robber 1. But we need to know if we choose the first house

'''
class Solution:
    def helper(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[1], nums[0])

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

             