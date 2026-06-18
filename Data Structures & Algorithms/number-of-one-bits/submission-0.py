# 



class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        i = 31

        while i >= 0:
            if 2 ** i <= n:
                count += 1
                n -= 2 ** i
            i -= 1

        return count
        
        