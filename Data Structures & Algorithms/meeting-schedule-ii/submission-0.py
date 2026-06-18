"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        roomEndTimeDict = {}
        intervals.sort(key=lambda interval: interval.start)

        for interval in intervals:
            foundRoom = False
            for key, value in roomEndTimeDict.items():
                if interval.start >= value:
                    roomEndTimeDict[key] = interval.end
                    foundRoom = True
                    break
        
            if not foundRoom:
                roomEndTimeDict[len(roomEndTimeDict)] = interval.end

        return len(roomEndTimeDict)
        
        