class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seenSet = set()
        res = set()

        for i, x in enumerate(nums):
            for y in nums[i + 1:]:
                z = -1 * (x + y)
                if z in seenSet:
                    res.add(tuple(sorted([x,y,z])))
            seenSet.add(x)
                
        return list(res)