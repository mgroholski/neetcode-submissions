class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetterMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        res = []
        def dfs(sol, digits):
            if len(digits) == 0:
                if len(sol):
                    nonlocal res
                    res.append(sol)
                return

            nonlocal numToLetterMap
            for l in numToLetterMap[digits[0]]:
                dfs(sol + l, digits[1:])

        dfs("", digits)
        return res
        