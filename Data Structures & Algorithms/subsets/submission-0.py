class Solution:
    def backtrack(self, nums, numsIdx, sol) -> List[List[int]] :        
        print(numsIdx, sol)
        
        n = len(nums)
        if numsIdx == n:
            return [sol]
        
        solutionSet = []
        solutionSet += self.backtrack(nums, numsIdx + 1, sol)
        solutionSet += self.backtrack(nums, numsIdx + 1, sol + [nums[numsIdx]])
        return solutionSet


    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(nums, 0, [])
        