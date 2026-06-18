'''
We can use dp to answer, what's the maximum subarray starting at point i?
    We either choose to combine with another subarray or stay alone

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            dp[i] = nums[i] + max(0, dp[i+1])

        return max(dp)

        