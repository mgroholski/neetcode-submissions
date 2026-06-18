# Merge over lapping intervals:
#   if start_b <= end_a


# Algorithm
# 1. Sort by start time
# for i in intervals
#   if start_b <= end_a
#       merge




class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda a : a[0])

        res = [intervals[0]]

        for i in intervals[1:]:
            if i[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)

        return res
        