class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chrSet = set()
        res = 0

        l = 0
        for r, val in enumerate(s):
            if val in chrSet:
                res = max(res, r - l)
                while val in chrSet:
                    chrSet.remove(s[l])
                    l += 1
            chrSet.add(val)

        res = max(res, len(s) - l)
        return res

            


        