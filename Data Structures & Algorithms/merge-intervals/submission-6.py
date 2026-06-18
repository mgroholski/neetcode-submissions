class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals.pop(0)]
        while intervals:
            u,v = res[-1]
            s,e = intervals.pop(0)

            if s <= v:
                res[-1][-1] = max(v,e)
            else:
                res.append([s,e])
        return res