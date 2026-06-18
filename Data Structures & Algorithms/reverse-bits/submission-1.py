class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        cnt = 32

        while n:
            res <<= 1
            if n & 1:
                res += 1
            cnt -= 1
            n >>= 1

        while cnt:
            res <<= 1
            cnt -= 1

        return res