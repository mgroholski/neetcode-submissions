class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lProd, rProd = [1] * len(nums), [1] * len(nums)

        for i in range(len(nums)):
            lIdx, rIdx = i, len(nums) - 1 - i
            
            l = 1
            if lIdx > 0:
                l = lProd[lIdx - 1]
            
            lProd[lIdx] = l * nums[lIdx]

            r = 1
            if rIdx < len(nums) - 1:
                r = rProd[rIdx + 1]
            rProd[rIdx] = r * nums[rIdx]

        res = []

        for idx in range(len(nums)):
            l, r = 1, 1

            if idx > 0:
                l = lProd[idx - 1]

            if idx < len(nums) - 1:
                r = rProd[idx + 1] 

            res.append(l * r)

        return res






        