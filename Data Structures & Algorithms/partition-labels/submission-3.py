class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterCnt = Counter(s)
        res = []

        r = 0
        letterSet = set()
        partitionReqCnt = 0
        for l in range(len(s)):
            if s[l] not in letterSet:
                letterSet.add(s[l])
                partitionReqCnt += letterCnt[s[l]]
            letterCnt[s[l]] -= 1
            partitionReqCnt -= 1

            if not partitionReqCnt:
                res.append(l - r  + 1)
                r = l + 1
                letterSet = set()

        return res