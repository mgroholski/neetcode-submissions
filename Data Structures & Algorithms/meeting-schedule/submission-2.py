"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda a : a.start)

        e_l = 0
        for interval in intervals:
            s, e = interval.start, interval.end
            if s < e_l:
                return False
            e_l = e

        return True
