'''
We want to find the fewest number of coins that you need to make up that amount.

Why can't we greedily take coins?
coins = [1,2,5], amount = 11
5 + 5 + 1 

We don't want to use dp on coins; use it on the amount. Why?
coins = [4, 3, 2, 1], amount = 13

4,4,4,1
4,4,3,2


coins = [1,2,5], amount = 11
[1,2,3]

For each amount, what is the min amount of coins to make it?

'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [-1 for _ in range(amount)]
        for a in range(amount):
            minCnt = float('inf')
            for coin in coins:
                if a - coin >= 0 and dp[a-coin] > 0:
                    minCnt = min(minCnt, dp[a - coin] + 1)
                elif coin == a + 1:
                    minCnt = min(minCnt, 1)
            dp[a] = minCnt if minCnt != float('inf') else -1

        return dp[-1]

        