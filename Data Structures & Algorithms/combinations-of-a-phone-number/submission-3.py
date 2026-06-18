# Construct digits map
# Enumerate all combination

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digitMapping = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }

        def backtrack(sol, digits):
            if len(digits) == 0:
                return [sol] if len(sol) else []
            
            solutions = []
            currentDigit = digits[0]
            digits = digits[1:]

            for i in self.digitMapping[currentDigit]:        
                solutions += backtrack(sol + i, digits)

            return solutions

        return backtrack("", digits)

        
            



        