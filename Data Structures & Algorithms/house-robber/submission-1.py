# Base case
#   dp[0] = nums[0]
#   dp[1] = nums[1]


# We can rob this house or not rob it
#   rob = dp[i - 2] + nums[i]
#   don't rob = dp[i - 1]


class Solution:
    def rob(self, nums: List[int]) -> int:        
        dp = [0] * (len(nums) + 2)
        
        for i in range(len(nums)):
            n = nums[i]
            i = i + 2
            dp[i] = max(dp[i - 1], dp[i - 2] + n)

        return dp[-1]


        