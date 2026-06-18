class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        expectedSum = int((n * (n + 1)) / 2)
        aSum = sum(nums)

        return expectedSum - aSum


        