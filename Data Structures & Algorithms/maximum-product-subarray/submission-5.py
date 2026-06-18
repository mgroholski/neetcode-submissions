class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]

        absDp = [1] * len(nums)
        absDp[0] = nums[0]

        maxVal = max(dp[0], absDp[0])

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] * nums[i], nums[i])

            if abs(absDp[i - 1] * nums[i]) >= abs(nums[i]):
                absDp[i] = absDp[i - 1] * nums[i]
            else:
                absDp[i] = nums[i]
            
            maxVal = max(dp[i], absDp[i], maxVal)

        print(dp, absDp)
        return maxVal
