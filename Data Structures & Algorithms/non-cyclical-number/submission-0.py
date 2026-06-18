class Solution:
    def isHappy(self, n: int) -> bool:
        seenSet = set([n])
        while n != 1:
            nStr = str(n)
            nSum = 0
            for i in nStr:
                nSum += int(i) ** 2

            if nSum in seenSet:
                return False
            else:
                seenSet.add(nSum)
                
            n = nSum
        return True



