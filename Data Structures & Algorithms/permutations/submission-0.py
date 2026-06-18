class Solution:
    def backtrack(self, sol, candidatesSet) -> List[List[int]]:
        if len(candidatesSet) == 0:
                return [sol]

        solutionList = []
        for i in candidatesSet:
                solutionList += self.backtrack(sol + [i], candidatesSet.difference(set({i})))
        return solutionList
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack([], set(nums))
        