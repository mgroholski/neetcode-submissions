class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chrDict = {}
        letterCnt = len(s1)

        for c in s1:
            if c not in chrDict:
                chrDict[c] = 0
            chrDict[c] += 1
        
        r = 0
        for l in range(len(s2)):
            c_l = s2[l]

            if c_l not in chrDict:
                while r < l + 1:
                    c_r = s2[r]
                    if c_r in chrDict:
                        chrDict[c_r] += 1
                        letterCnt += 1
                    r += 1
            else:
                chrDict[c_l] -= 1
                letterCnt -= 1
                while chrDict[c_l] < 0:
                    c_r = s2[r]
                    chrDict[c_r] += 1
                    letterCnt += 1
                    r += 1
                if not letterCnt:
                    return True

        return False