'''
At any point, you can either 
1. open a parenthesis if n
2. close a parenthesis if 

'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(n, s, a):
            if not n and not a:
                nonlocal res
                res.append(s)

            if n > 0:
                dfs(n - 1, s + "(", a + 1)
            
            if a > 0:
                dfs(n, s + ")", a - 1)

        dfs(n, "", 0)
        return res
        