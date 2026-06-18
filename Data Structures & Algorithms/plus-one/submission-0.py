class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        carry = 0

        digits[idx] += 1
        if digits[idx] > 9:
            carry = 1
            digits[idx] %= 10
        idx -= 1
        
        while carry and idx >= 0:
            digits[idx] += 1
            carry = digits[idx] > 9
            digits[idx] %= 10
            idx -= 1  

        if carry:
            digits.insert(0, 1)
        
        return digits
        