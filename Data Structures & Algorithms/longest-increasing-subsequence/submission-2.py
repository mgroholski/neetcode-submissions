class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(1, len(nums)):
            maxVal = 1
            for j in range(0,i):
                if nums[j] < nums[i]:
                    maxVal = max(dp[j] + 1, maxVal)
            dp[i] = maxVal
        return max(dp)
        