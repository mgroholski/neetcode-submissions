class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                return False
        tFreqDict = {}
        for character in t:
                if character in tFreqDict:
                        tFreqDict[character] += 1
                else:
                        tFreqDict[character] = 1
        for character in s:
                if character in tFreqDict and tFreqDict[character] > 0:
                        tFreqDict[character] -= 1
                else:
                        return False
        return True