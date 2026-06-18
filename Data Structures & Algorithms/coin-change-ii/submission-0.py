'''
Integer amount and array coins. 
Return the amount of combinations that total up to amount.
If one doesn't exist return 0.

amount = 4, coins = [1,2,3]

'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        dp[0][0] = 1

        for i in range(1, len(coins) + 1):
            newCoin = coins[i - 1]
            for j in range(0, amount + 1):
                dp[i][j] = dp[i - 1][j]

                if j - newCoin >= 0:
                    dp[i][j] += dp[i][j - newCoin]

        return dp[-1][-1]
                
        