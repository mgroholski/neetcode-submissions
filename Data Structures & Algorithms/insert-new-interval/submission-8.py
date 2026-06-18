'''
Find position where newInterval would be inserted
if new interval overlaps combine them

intervals = [[1,6]], newInterval = [2,5]


intervals = [[1,2],[3,5],[6,7],[9,10]], newInterval = [6,7]

Algorithm
Binary Search for insertion position O(log n)
Check if i - 1 end time and i start time overlap:
    if so combine

Check if i + 1 start time and i end time overlap:
    if so combine

return new List
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []

        inserted = False
        for i, val in enumerate(intervals):
            if not inserted and newInterval[0] < val[0]:
                if len(newIntervals) and newInterval[0] <= newIntervals[-1][1]:
                    newIntervals[-1][1] = max(newInterval[1], newIntervals[-1][1])
                else:
                    newIntervals.append(newInterval)

                inserted = True

                print(newIntervals[-1][1], val[0])
                if newIntervals[-1][1] >= val[0]:
                    newIntervals[-1][1] = max(val[1], newIntervals[-1][1])
                else:
                    newIntervals.append(val)
            else:
                if len(newIntervals) and val[0] <= newIntervals[-1][1]:
                    newIntervals[-1][1] = max(val[1], newIntervals[-1][1])
                else:
                    newIntervals.append(val)

        if not inserted:
            if len(newIntervals) and newInterval[0] <= newIntervals[-1][1]:
                    newIntervals[-1][1] = max(newInterval[1], newIntervals[-1][1])
            else:
                newIntervals.append(newInterval)

        return newIntervals






