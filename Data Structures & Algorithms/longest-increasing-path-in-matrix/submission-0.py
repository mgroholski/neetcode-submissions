class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp = {}

        def dfs(pos, prevVal):
            x,y = pos
            if x >= m or x < 0 or y < 0 or y >= n or matrix[x][y] <= prevVal:
                return 0
            
            if pos in dp:
                return dp[pos]

            currentVal = matrix[x][y]

            res = max(1, 
            1 + dfs((x + 1, y), currentVal),
            1 + dfs((x - 1, y), currentVal),
            1 + dfs((x, y + 1), currentVal),
            1 + dfs((x, y - 1), currentVal)
            )

            dp[pos] = res
            return res

        sol = 1
        for x in range(m):
            for y in range(n):
                sol = max(sol, dfs((x, y), -1))
        return sol





