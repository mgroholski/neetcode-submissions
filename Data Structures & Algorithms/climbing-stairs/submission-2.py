class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        fMinusOne = 2
        fMinusTwo = 1
        totalAmount = 0
        i = 3
        while i <= n: #O(n)
            totalAmount = fMinusOne + fMinusTwo
            fMinusTwo = fMinusOne
            fMinusOne = totalAmount
            i += 1

        return totalAmount