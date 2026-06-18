class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            minAmount = float('inf')
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] >= 0:
                    minAmount = min(1 + dp[i - coin], minAmount)
            if minAmount != float('inf'):
                dp[i] = minAmount
                
        return dp[-1]

        