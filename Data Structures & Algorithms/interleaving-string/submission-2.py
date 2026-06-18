'''
We want to see if s3 can be composed of s1 and s2

There's three options:

Let x be the head of s3:
    x comes from s1
    x comes from s2
    x can come from either 

The first two are trivial. We need to determine what happens if it can come from either

We can use 2D dp to determine wher 
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not len(s1) + len(s2) == len(s3):
            return False
        

        dp = [[False for _ in range((len(s2) + 1))] for _ in range(len(s1) + 1)]
        dp[-1][-1] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if (i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]) or j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j]=True

        return dp[0][0]
                
        
        