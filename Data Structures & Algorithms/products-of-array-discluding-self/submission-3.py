class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        r = [1] * len(nums)

        p = 1
        q = 1
        for i in range(len(nums)):
            p *= nums[i]
            q *= nums[len(nums) - 1 - i]
            l.append(p)
            r[len(nums) - 1 - i] = q

        res = []
        for idx in range(len(nums)):
            b = l[idx - 1] if idx > 0 else 1
            a = r[idx + 1] if idx < len(nums) - 1 else 1

            res.append(b * a)
        return res

        
            




        

        