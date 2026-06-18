class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = 0
            
            if digits[i] > 9:
                carry = digits[i] // 10
                digits[i] = digits[i] % 10

        if carry:
            digits = [carry] + digits

        return digits