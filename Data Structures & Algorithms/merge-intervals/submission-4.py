'''
Goal: Merge all overlapping intervals

We'll want to sort the array by start interval, end interval

What types of overlap are there:
    1. end_i >= start_j
        i. end_j <= end_i 
        ii. end_j > end_i
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])
        
        res = []
        l_s, l_e = intervals[0]
        for i in range(1, len(intervals)):
            s,e = intervals[i]
            if l_e >= s:
                l_e = max(l_e, e)
            else:
                res.append([l_s,l_e])
                l_s, l_e = s,e
        
        res.append([l_s, l_e])
        return res


        