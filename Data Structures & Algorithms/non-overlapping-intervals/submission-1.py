# Return the minimum amount of intervals to make the set non-overlapping

# Overlapping:
#   if start_a < end_b (can share a common point)


# If two are overlapping:
#   Remove a or b


# Sort by:
# 1. Start time (lowest first)
# 2. End time (lowest first)

# Create timelines for non-overlapping interval
#   Each timeline that doesn't fit into a prexiting one gets a new one
# Remove timelines with least intervals until one remains
# Return amount of intervals removed


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], interval[1]))

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prevEnd:
                res += 1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end
        
        return res