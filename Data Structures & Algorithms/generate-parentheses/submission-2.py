'''
At any given point we can,
1. Close a parenthesis (if one is open)
2. Open a parenthesis (if another one is needed)


'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(s, n, o):
            if not n and not o:
                nonlocal res
                res.append(s)
                return

            if n:
                generate(s + "(", n - 1, o + 1)
            
            if o:
                generate(s + ")", n, o - 1)

        generate("", n, 0)
        return res
        