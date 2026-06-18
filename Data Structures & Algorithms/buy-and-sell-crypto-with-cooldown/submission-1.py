'''
prices where prices[i] is the price of on the ith day.

Rules:
After you sell, you cannot buy another one on the next day.
You may only own at most one at a time.

Return max profit

'''



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * len(prices) for _ in prices]

        for i in range(len(prices) - 2, -1, -1):
            for j in range(len(prices) - 1, i - 1, -1):
                holdValue = dp[i][j + 1] if j + 1 < len(prices) else 0
                sellValue = prices[j] - prices[i]
                passValue = dp[i + 1][i + 1]

                if j + 2 < len(prices):
                    sellValue += dp[j + 2][j + 2]

                dp[i][j] = max(passValue, holdValue, sellValue)

        print(dp)
        return dp[0][0]

        