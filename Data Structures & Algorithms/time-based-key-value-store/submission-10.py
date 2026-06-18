'''
Use a double map

key -> time -> value

'''

from sortedcontainers import SortedDict

class TimeMap:
    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = SortedDict()
        self.map[key][timestamp] = value
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
    
        it = self.map[key].bisect_right(timestamp)
        if it == 0:
            return ""

        return self.map[key].peekitem(it - 1)[1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)