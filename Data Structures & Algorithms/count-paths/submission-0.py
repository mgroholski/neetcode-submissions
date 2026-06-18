'''
m x n grid where you are allowed to move 
either down or to the right at any point in time.

Given the two integers m and n, return the amount of unique possible paths 
from the top corner to the bottom left corner.
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
        