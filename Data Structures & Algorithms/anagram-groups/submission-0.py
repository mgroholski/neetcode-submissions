class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seenDict = {}
        for i in strs:
            sortedStr = ''.join(sorted(i))
            if sortedStr in seenDict:
                seenDict[sortedStr].append(i)
            else:
                seenDict[sortedStr] = [i]
        results = []
        for arr in seenDict.values():
            results.append(arr)
        return results