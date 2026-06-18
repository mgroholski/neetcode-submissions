class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        bin_n = bin(n)

        one_cnt = 0
        for i in bin_n:
            if i == '1':
                one_cnt += 1

        return one_cnt == 1
        