# Base case
#   dp[0] = nums[0]
#   dp[1] = nums[1]


# We can rob this house or not rob it
#   rob = dp[i - 2] + nums[i]
#   don't rob = dp[i - 1]


class Solution:
    def rob(self, nums: List[int]) -> int:        
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            oneHouse = 0 if i < 1 else dp[i - 1]
            twoHouses = 0 if i < 2 else dp[i - 2]

            dp[i] = max(oneHouse, twoHouses + nums[i])
        return dp[-1]


        