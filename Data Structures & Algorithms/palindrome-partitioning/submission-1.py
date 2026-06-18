class Solution:
    def backtrack(self, sol, s) -> List[List[str]]:
        if not s:
            for i in sol:
                if i != i[::-1]:
                    return []
            return [sol]

        solutionList = []
        # Add
        if len(sol):
            appendedLastElement = sol[-1] + s[0]
            solutionList += self.backtrack(sol[:-1] + [appendedLastElement], s[1:])

        # Start
        solutionList += self.backtrack(sol + [s[0]], s[1:])
        return solutionList

    def partition(self, s: str) -> List[List[str]]:
        return self.backtrack([], s)
        
        

