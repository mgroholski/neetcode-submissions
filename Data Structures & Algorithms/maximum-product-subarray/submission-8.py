class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxDp = [float('-inf')] * len(nums)
        maxDp[0] = nums[0]

        minDp = [float('inf')] * len(nums)
        minDp[0] = nums[0]

        for i in range(1, len(nums)):
            maxDp[i] = max(minDp[i - 1] * nums[i], maxDp[i-1] * nums[i], nums[i])
            minDp[i] = min(minDp[i - 1] * nums[i], maxDp[i - 1] * nums[i], nums[i])

        return max(maxDp)
