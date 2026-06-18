'''
123 * 456

123 * 6 = (100 * 6) + (20 * 6) + (3 * 6)
123 * 50 = (100 * 50) + ()
123 * 400

'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0

        i_multiplier = 0
        for i in num1[::-1]:
            j_multiplier = 0
            for j in num2[::-1]:
                res += (int(i) * (10 ** i_multiplier) * int(j) * (10 ** j_multiplier)) 
                j_multiplier += 1

            i_multiplier += 1

        return str(res)
                