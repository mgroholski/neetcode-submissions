'''
We can use a two pointer approach. We only want to shorten the window when k < 0 

How do we know how many letters are not apart of the majority letter?
    We don't actually need to know the majority letter just the max amount of a single letter we've seen within a window. Res will be cnt + k

s = "AABABBA", k = 1

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        cnt = {}
        maxCnt = 0

        l = 0
        for r in range(len(s)):
            letter = s[r]
            if letter not in cnt:
                cnt[letter] = 0
            cnt[letter] += 1

            maxCnt = max(cnt[letter], maxCnt)

            while r - l + 1 - maxCnt > k:
                cnt[s[l]] -= 1
                l += 1
                
            res = max(r - l + 1, res)
        return res





        