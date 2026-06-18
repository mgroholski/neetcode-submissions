'''
Given word1 and word2

You can perform three operations:
1. insert a character at any position
2. delete a character at any position
3. replace a character at any position

return the minimum number of operations to make word1 equal word2

'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1)):
            dp[i][-1] = len(word1) - i
        
        for i in range(len(word2)):
            dp[-1][i] = len(word2) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                rightVal = dp[i][j + 1] + 1
                downVal = dp[i + 1][j] + 1
                matchVal = dp[i + 1][j + 1] + 1
                
                if word1[i] == word2[j]:
                    matchVal = dp[i + 1][j + 1]
                
                dp[i][j] = min(rightVal, downVal, matchVal)

        return dp[0][0]


        