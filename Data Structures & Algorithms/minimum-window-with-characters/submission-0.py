'''
 Find the minimum substring of s such that all characters in t are contained
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT = {}
        lastIdxDict = {}

        for i in t:
            if i not in freqT:
                freqT[i] = 0
            freqT[i] += 1

            if i not in lastIdxDict:
                lastIdxDict[i] = []

        foundLetters = 0
        shortestSubstring = None

        l, r = 0, 0
        while r < len(s):
            rightLetter = s[r]
            if rightLetter in t:
                foundLetters += 1
                lastIdxDict[rightLetter].append(r)

                while len(lastIdxDict[rightLetter]) > freqT[rightLetter]:
                    lastIdxDict[rightLetter].pop(0)
                    foundLetters -= 1

                if foundLetters == len(t):
                    minDictVal = float('inf')
                    for val in lastIdxDict.values():
                        minDictVal = min(val[0], minDictVal)
                    l = minDictVal

                    if not shortestSubstring or r - l < len(shortestSubstring):
                        shortestSubstring = s[l:r + 1]
            r += 1

        return "" if shortestSubstring is None else shortestSubstring
            


        