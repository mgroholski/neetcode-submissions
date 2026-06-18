class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterIntervals = {}

        for idx, l in enumerate(s):
            if l not in letterIntervals:
                letterIntervals[l] = [idx,idx]
            else:
                letterIntervals[l][1] = idx

        intervals = sorted(letterIntervals.values())
        
        res = []
        s, e = intervals[0]
        for a, b in intervals[1:]:
            if a <= e and b > e:
                e = b
            elif a > e:
                res.append(e - s + 1)
                s,e = a,b

        res.append(e - s + 1)

        return res


