# s = "xyxxyzbzbbisl"

# Algorithm
# Find first and last index of each letter
# if letter != endLetter:
#   endIdx = max(letter[end], endLetter[end])
#   endLetter = which ever letter chosen
# if reached endIdx then append res with length of substring




class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idxDict = {}

        for i in range(len(s)):
            idxDict[s[i]] = i

        res = []

        # How to start?
        currentIdx = 0
        startIdx = 0
        endIdx = 0
        endLetter = None
        while currentIdx < len(s):
            if not endLetter or (endLetter != s[currentIdx] and idxDict[s[currentIdx]] > endIdx):
                endIdx = idxDict[s[currentIdx]]
                endLetter = s[currentIdx]

            if currentIdx == endIdx:
                res.append(endIdx - startIdx + 1)
                startIdx = currentIdx + 1

            currentIdx += 1

        return res

        