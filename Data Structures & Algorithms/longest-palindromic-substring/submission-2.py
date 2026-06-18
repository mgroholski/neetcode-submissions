class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = ""

        for i in range(len(s)):
            l,r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(longestPalindrome):
                    longestPalindrome = s[l:r + 1]
                r += 1
                l -= 1

            l,r = i, i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(longestPalindrome):
                    longestPalindrome = s[l:r+1]
                r += 1
                l -= 1

        return longestPalindrome

        