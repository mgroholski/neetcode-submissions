class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        idx_dict = {}
        for idx, i in enumerate(nums):
            k = target - i
            if k in seen:
                return [idx_dict[k],idx]
            seen.add(i)
            idx_dict[i] = idx

        return None
            
        