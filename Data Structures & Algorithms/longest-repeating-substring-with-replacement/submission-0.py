class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqDict = {}
        dominantLetter = None
        startIdx = 0
        currentK = 0
        longestLength = 0

        for i, val in enumerate(s):
            if val in freqDict:
                    freqDict[val] += 1
            else:
                    freqDict[val] = 1

            if not dominantLetter or freqDict[val] > freqDict[dominantLetter]:
                    dominantLetter = val

            currentK = i - startIdx + 1 - freqDict[dominantLetter]
            print(dominantLetter, startIdx, i, currentK)
            while currentK > k:
                freqDict[s[startIdx]] -= 1
                startIdx += 1
                for j in freqDict.keys():
                        if freqDict[j] > freqDict[dominantLetter]:
                                dominantLetter = j
                currentK = i - startIdx + 1 - freqDict[dominantLetter]
            longestLength = max(i - startIdx + 1, longestLength)

        return max(longestLength, len(s) - startIdx)
        