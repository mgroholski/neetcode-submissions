class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = Counter(s)
        letterCnt = 0
        for i in t:
            if i in freqS and freqS[i] > 0:
                    freqS[i] -= 1
            else:
                return False

            letterCnt += 1

        return letterCnt == len(s)


        
        