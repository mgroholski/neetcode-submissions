class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            streak = 1
            if (n - 1) not in numSet:
                while n + 1 in numSet:
                    streak += 1
                    n = n + 1

            res = max(streak, res)

        return res
        