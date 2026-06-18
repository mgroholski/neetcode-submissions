class Solution:
    def backtrack(self, sol: str, n: int, stackLength: int) -> List[str]:
        if n == 0 and stackLength == 0:
            return [sol]
        
        solutionList = []
        if n > 0:
            solutionList += self.backtrack(sol + "(", n - 1, stackLength + 1)
        
        if stackLength > 0:
            solutionList += self.backtrack(sol + ")", n, stackLength - 1)
        
        return solutionList
    
    def generateParenthesis(self, n: int) -> List[str]:
        return self.backtrack("", n, 0)
        