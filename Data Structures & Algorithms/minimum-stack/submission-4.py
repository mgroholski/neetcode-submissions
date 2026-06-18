class MinStack:
    def __init__(self):
        self.stack = []
        self.heap = []
        self.elementsCnt = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap, val)
        if val not in self.elementsCnt:
            self.elementsCnt[val] = 0
        self.elementsCnt[val] += 1

    def pop(self) -> None:
        val = self.stack.pop()
        self.elementsCnt[val] -= 1
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        while not self.elementsCnt[self.heap[0]] > 0:
            heapq.heappop(self.heap)

        return self.heap[0]

            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()