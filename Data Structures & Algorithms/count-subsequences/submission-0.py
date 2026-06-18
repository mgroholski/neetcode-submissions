'''
Given two strings s ant t, return the number of distinct subsequences of s which equal t.
'''


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

        dp[-1][-1] = 1

        for i in range(len(s) + 1):
            dp[-1][i] = 1

        for j in range(len(t) - 1, -1, -1):
            for i in range(len(s) - 1, -1, -1):
                val = dp[j][i + 1]

                if t[j] == s[i]:
                    val += dp[j + 1][i + 1]

                dp[j][i] = val

        return dp[0][0]