'''
We need to find a subset with neededSum
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        neededSum = total // 2 # We need to find a subset with sum neededSum

        seen = set([0])
        for i in nums:
            for j in seen.copy():
                if i + j == neededSum:
                    return True
                if i + j < neededSum:
                    seen.add(i+j)
            seen.add(i)

        return False

            
