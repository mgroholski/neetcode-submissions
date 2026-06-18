class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Shift l if character is not alphanumeric
            while l < r and not ('a' <= s[l].lower() <= 'z' or '0' <= s[l] <= '9'):
                l += 1

            while l < r and not ('a' <= s[r].lower() <= 'z' or '0' <= s[r] <= '9'):
                r -= 1

            if (s[l].lower() != s[r].lower()):
                return False

            l += 1
            r -= 1

        return True


