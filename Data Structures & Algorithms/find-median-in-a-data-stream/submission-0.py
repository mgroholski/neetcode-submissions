class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.median = None
        

    def addNum(self, num: int) -> None:
        if self.median is None:
            self.median = num
            heapq.heappush(self.minHeap, num)
        elif self.median > num:
            heapq.heappush(self.maxHeap, -1 * num)
        else:
            heapq.heappush(self.minHeap, num)

        # Balance heaps and find new median
        while abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                minHeapElement = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -1 * minHeapElement)
            else:
                maxHeapElement = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -1 * maxHeapElement)

        if (len(self.minHeap) + len(self.maxHeap)) % 2:
            if len(self.minHeap) > len(self.maxHeap):
                self.median = self.minHeap[0]
            else:
                self.median = -1 * self.maxHeap[0]
        else:
            maxHeapElement = -1 * self.maxHeap[0]
            minHeapElement = self.minHeap[0]
            self.median = (maxHeapElement + minHeapElement) / 2

    
    def findMedian(self) -> float:
        return self.median
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()