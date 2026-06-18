import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._heap = nums
        heapq.heapify(self._heap)
        self._k = k

    def add(self, val: int) -> int:
        heapq.heappush(self._heap, val)
        return heapq.nlargest(self._k, self._heap)[-1]
        
