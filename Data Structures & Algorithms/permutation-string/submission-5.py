class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1FreqDict = {}
        for i in s1:
            if i in s1FreqDict:
                s1FreqDict[i] += 1
            else:
                s1FreqDict[i] = 1
    
        for startIdx in range(len(s2) - len(s1) + 1):
            s2Substring = s2[startIdx: startIdx + len(s1)]
            s1FreqDictCopy = s1FreqDict.copy()
            validSubstring = True
            for j in s2Substring:
                    if not j in s1FreqDictCopy or s1FreqDictCopy[j] == 0:
                        validSubstring = False
                        break
                    else:
                        s1FreqDictCopy[j] -= 1
            if validSubstring:
                    return True
        return False
        
        