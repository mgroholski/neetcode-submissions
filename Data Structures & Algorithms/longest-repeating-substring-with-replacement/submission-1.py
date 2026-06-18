'''
Find longest string such that there's only k nondominant letters.

O(1) for switching dominant letters (only 26 options)

'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {chr(i+ord('A')) : 0 for i in range(26)}  

        res = 0
        l = 0 
        for r in range(len(s)):
            freq[s[r]] += 1

            while sum(freq.values()) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
            


        