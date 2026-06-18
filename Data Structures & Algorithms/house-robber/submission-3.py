class Solution:
    def rob(self, nums: List[int]) -> int:
        twoBefore = 0
        oneBefore = 0

        for i in range(len(nums) - 1, -1, -1):
            score = max(nums[i] + twoBefore, oneBefore)
            twoBefore = oneBefore
            oneBefore = score

        return oneBefore



        