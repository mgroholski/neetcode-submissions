import math

class TimeMap:
    def __init__(self):
        self._timeBasedMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self._timeBasedMap:
            self._timeBasedMap[key].append((value, timestamp))
        else:
            self._timeBasedMap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._timeBasedMap:
            return ""
        
        arr = self._timeBasedMap[key]
        l = 0
        r = len(arr) - 1

        while l < r:
            mid = (l + r) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        
        if arr[l][1] <= timestamp:
            return arr[l][0]
        elif arr[l][1] > timestamp and l - 1 >= 0:
            return arr[l - 1][0]
        else:
            return ""





        
