class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [0 for _ in range(len(s))]
        dp[0] = 1

        for i in range(1, len(s)):
            c = s[i]
            if c > '0':
                dp[i] += dp[i - 1] # Decode as single character
            if s[i - 1] in "1" or (s[i-1] == "2" and c <= "6"):
                dp[i] += dp[i - 2] if i - 2 >= 0 else 1
            
        return dp[-1]
        