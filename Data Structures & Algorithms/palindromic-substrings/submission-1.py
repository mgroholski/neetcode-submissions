'''
We want to build palindromic substrings

for i in string
    i could be the middle of the palindromic substring

we either 
1. expand both sides 
    If we expand both sides, we consider another round of expansion
2. expand a single side
    If we expand a single side, we stop building
'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for idx, i in enumerate(s):
            l, r = idx, idx
            while l >= 0 and r < len(s) and s[l:r + 1] == s[l:r + 1][::-1]:
                res += 1
                l -= 1
                r += 1

            l,r = idx, idx + 1
            while l >= 0 and r < len(s) and s[l:r + 1] == s[l:r + 1][::-1]:
                res += 1
                l -= 1
                r += 1

        return res


        