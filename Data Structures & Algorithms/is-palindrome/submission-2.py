class Solution:
    def isAlphanumeric(self, s: str) -> bool:
        if len(s) != 1:
            return False
        
        return (s >= '0' and s <= '9') or (s.lower() >= 'a' and s.lower() <= 'z')

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while i < len(s) and not self.isAlphanumeric(s[i]):
                i += 1
            while j >= 0 and not self.isAlphanumeric(s[j]):
                j -= 1

            if i >= j:
                break
            
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True

        