'''
We'll brute force the solution. If it doesn't work we can use a cache.

'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.res = set()
        
        def dfs(sol, idx, target):
            if not target or (self.candidates[0] > target) or idx >= len(self.candidates):
                if not target:
                    self.res.add(tuple(sol))
                return

            for i in range(idx, len(self.candidates)):
                dfs(sol + [self.candidates[i]], i, target - self.candidates[i])

        self.candidates.sort()
        dfs([], 0, target)
        return [list(i) for i in self.res]
        