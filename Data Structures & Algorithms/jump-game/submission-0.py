class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]