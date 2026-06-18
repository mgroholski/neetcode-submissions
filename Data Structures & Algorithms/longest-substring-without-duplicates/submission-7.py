class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        longestSubset = 0
        seenDict = {}
        startIdx = 0
        for i, val in enumerate(s):
            if val in seenDict and seenDict[val] >= startIdx:
                longestSubset = max(i - startIdx, longestSubset)
                startIdx = seenDict[val] + 1
                seenDict[val] = i
                # print(val, seenDict)
            else:
                seenDict[val] = i
        print(startIdx)
        return max(len(s) - startIdx, longestSubset)