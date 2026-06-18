class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for i in nums:
                if i in freqDict:
                        freqDict[i] += 1
                else:
                        freqDict[i] = 1
        kMost = []
        for i in freqDict.keys():
                inserted = False
                for j in range(len(kMost)):
                        if freqDict[i] > kMost[j][1]:
                                kMost.insert(j, (i, freqDict[i]))
                                inserted = True
                                break       
                if not inserted and len(kMost) < k:
                        kMost.append((i, freqDict[i]))
                else:
                        kMost = kMost[:k]
        ans = []
        for i in kMost:
                ans.append(i[0])
        return ans