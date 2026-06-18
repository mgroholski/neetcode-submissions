class Solution:
    def reverseBits(self, n: int) -> int:
        i = 31
        returnVal = 0

        while i >= 0:
            currentBitVal = 2 ** i
            if currentBitVal <= n:
                returnVal += 2 ** (31 - i)
                n -= currentBitVal
            i -= 1

        return returnVal
        