'''
We can reduce the number of recursion calls 
a^(a+b) = a^a * a^b

'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == -1:
            return 1/x
        if n == 0:
            return 1

        if not n % 2:
            a = self.myPow(x, n // 2)
            return a * a
        else:
            a = self.myPow(x, n // 2)
            b = self.myPow(x, n // 2 + 1)
            return a * b
        
        