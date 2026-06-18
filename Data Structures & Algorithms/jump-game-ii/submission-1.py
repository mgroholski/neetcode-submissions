'''
We can solve this in a DP manner

nums = [2,3,1,1,4]
[0,1,1,2,2]


'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf') for _ in range(len(nums))]
        dp[0] = 0

        for i in range(len(nums)):
            for j in range(1,nums[i] + 1):
                if i + j < len(nums):
                    dp[i + j] = min(dp[i] + 1, dp[i + j])

        return dp[-1]

        
        
        