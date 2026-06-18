class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        res = 0
        for i in nums:
            cnt = 1
            if i - 1 not in numsSet:
                while i + 1 in numsSet:
                    cnt += 1
                    i += 1
            res = max(res, cnt)

        return res
        