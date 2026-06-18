class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, hold, reset = float('-inf'), float('-inf'), 0
        for price in prices:
            sold,hold,reset = price+hold, max(reset-price, hold), max(reset, sold)

        return max(reset, sold)