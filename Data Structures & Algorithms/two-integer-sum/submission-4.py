class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, i in enumerate(nums):
            k = target - i
            if k in seen.keys():
                return [seen[k], idx]
            
            seen[i]=idx
            