class Solution:
    def backtrack(self, sol, target, candidates):
        if target == 0:
            return [sol]
        elif target < 0 or len(candidates) == 0:
            return []

        solutionList = []
        while len(candidates) > 0:
            candidate = candidates[0]
            solutionList += self.backtrack(sol + [candidate], target - candidate, candidates)
            candidates = candidates[1:]

        return solutionList

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.backtrack([], target, candidates)