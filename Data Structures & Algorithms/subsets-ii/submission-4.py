class Solution:
    def backtrack(self, sol, candidates: List[int]):
        if len(candidates) == 0:
            return set([tuple(sorted(list(sol)))])
        
        solSet = set()
        candidate = candidates[0]
        candidates = candidates[1:]
        solList = list(sol)
        solSet = solSet.union(self.backtrack(tuple(solList + [candidate]), candidates))
        solSet = solSet.union(self.backtrack(sol, candidates))
        return solSet

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = self.backtrack((), nums)
        resultsAsList = []
        for i in results:
            resultsAsList.append(list(i))
        return resultsAsList