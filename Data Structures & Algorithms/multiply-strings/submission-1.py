class Solution:
    def convertStringToInt(self, a) -> int:
        aInt = 0
        factor = 0

        for i in range(len(a) - 1, -1, -1):
            aInt += (ord(a[i]) - ord('0')) * (10 ** factor)
            factor += 1

        return aInt

    def multiply(self, num1: str, num2: str) -> str:
        num1Int = self.convertStringToInt(num1)
        num2Int = self.convertStringToInt(num2)

        res = num1Int * num2Int

        if res == 0:
            return "0"

        resString = ""
        while res > 0:
            digit = res % 10
            resString = chr(digit + ord('0')) + resString
            res //= 10

        return resString

        