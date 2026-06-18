'''

'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(sol, s):
            if not len(s):
                res.append(sol.copy())
                return 

            for r in range(1, len(s) + 1):
                substr = s[:r]
                if substr == substr[::-1]:
                    sol.append(substr)
                    backtrack(sol, s[r:])
                    sol.pop()

        backtrack([], s)
        return res
    