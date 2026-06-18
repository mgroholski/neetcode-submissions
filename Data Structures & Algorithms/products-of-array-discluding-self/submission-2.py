class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        left[0], right[-1] = nums[0], nums[-1]

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i]
            rightIdx = len(nums) - 1 - i
            right[rightIdx] = right[rightIdx + 1] * nums[rightIdx]

        res = []
        for i in range(len(nums)):
            prod = 1
            if i > 0:
                prod *= left[i - 1]
            if i < len(nums) - 1:
                prod *= right[i + 1]

            res.append(prod)

        return res

                
        