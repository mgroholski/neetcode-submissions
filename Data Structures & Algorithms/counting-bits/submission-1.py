import math

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]

        output = [0, 1]

        i = 2
        while i <= n:
            sigBit = int(math.log(i) / math.log(2))
            output.append(1 + output[i - (2 ** sigBit)])
            i += 1
            
        return output
        