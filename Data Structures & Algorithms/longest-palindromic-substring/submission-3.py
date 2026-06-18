'''
Palindromic string is equal forwards and backwards. We want to consider cases with even and odd amount of characters 

s = "babad"

Brute force
We can use enumeration to either 
1. Skip a letter
2. Include a letter

If during this process the string is a palindrome, copy it down.

However, we can build palindromes from smaller palindromes if the two outsides are equal. 


s = "babad"
1. Each letter starts as a palindrome
2. We can add two or one


'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]

        # Start from 1
        for i in range(len(s)):
            l,r = i - 1, i + 1

            while 0 <= l and len(s) > r and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
                
        # Start from 2
        for i in range(len(s) - 1):
            l,r = i, i + 1
            while 0 <= l and len(s) > r and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1

        return res

        