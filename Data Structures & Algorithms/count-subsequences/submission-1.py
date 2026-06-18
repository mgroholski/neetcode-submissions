'''
Given two strings s ant t, return the number of distinct subsequences of s which equal t.
'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        lastRow = [1] * (len(s) + 1)

        for j in range(len(t) - 1, -1, -1):
            newRow = [0] * (len(s) + 1)

            for i in range(len(s) - 1, -1, -1):
                val = newRow[i + 1]

                if t[j] == s[i]:
                    val += lastRow[i + 1]

                newRow[i] = val
            
            lastRow = newRow

        return lastRow[0]