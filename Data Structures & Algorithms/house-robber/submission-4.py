'''
We want to maximize the amount stolen. Thus, we could choose to rob every house if possible. This is a dp problem, for each house we can choose to rob the adjacent house or rob two houses over and this house.

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]