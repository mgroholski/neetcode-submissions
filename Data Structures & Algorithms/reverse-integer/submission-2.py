class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)
        negative = False
        if x < 0:
            negative = True
            a = a[1:]
        
        result = int(a[::-1]) * (-1 if negative else 1)
        if result > 2**32:
            return 0
        
        return result
        