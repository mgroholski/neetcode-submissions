class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        n_s, n_e = newInterval
        while intervals:
            s,e = intervals.pop(0)

            if (e < n_s):
                res.append([s,e])
            elif n_e < s:
                intervals = [[s,e]] + intervals
                break
            else:
                n_s, n_e = min(n_s, s), max(n_e, e)
        
        res.append([n_s, n_e])
        res += intervals
        
        return res

        