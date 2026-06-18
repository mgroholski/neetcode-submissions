'''
Three strings s1, s2, and s3
Return true if s3 is formed by interleaving s1 and s2 together else false

Interleaving two strings s and t is done by dividing s and t into n and m
substrings respectively, such that

1. |n-m|<=1 (the difference between the amount of substrings is one)
2. s = s1 + s2 + ... + sn
3. t = t1 + t2 + ... + tm
4. Interleaving s and t is s1 + t1 + s2 + t2 + ... or vice-versa

'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[-1][-1] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]
        