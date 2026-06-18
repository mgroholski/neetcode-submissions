class Solution:
    def helper(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            oneAway = 0 if i < 1 else dp[i - 1]
            twoAway = 0 if i < 2 else dp[i - 2]
            dp[i] = max(oneAway, twoAway + nums[i])
        return dp[-1]
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        


            
        