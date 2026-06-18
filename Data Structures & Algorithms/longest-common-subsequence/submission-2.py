'''
2d DP problem. Reminds me of pattern matching 
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                a,b = text1[i], text2[j]    

                if a == b:
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] = max(dp[i-1][j-1], dp[i][j])
                    dp[i][j] += 1
                else:    
                    if i - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j])
                    if j - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i][j-1])

        return dp[-1][-1]
        