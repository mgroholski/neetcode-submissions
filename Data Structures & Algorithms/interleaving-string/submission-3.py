class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        m,n = len(s1) + 1, len(s2) + 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = True

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + j < len(s3):
                    if (i < len(s1) and s3[i + j] == s1[i]):
                        dp[i][j] = dp[i][j] or dp[i + 1][j]
                    if (j < len(s2) and s3[i + j] == s2[j]):
                        dp[i][j] = dp[i][j] or dp[i][j + 1]

        return dp[0][0]
        