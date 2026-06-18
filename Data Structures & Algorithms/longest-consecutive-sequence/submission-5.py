class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        res = 0
        for i in nums:
            curNum = i
            l = 1

            while curNum + 1 in numSet:
                l += 1
                curNum += 1
            
            res = max(l, res)

        return res

