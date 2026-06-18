"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda a: (a.start, a.end))
        
        minHeap = []
        for a in intervals:
            s,e = a.start, a.end
            if minHeap and minHeap[0] <= s:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, e)

        return len(minHeap)
        