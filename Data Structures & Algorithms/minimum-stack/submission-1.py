class MinStack:

    def __init__(self):
        self._stack = []
        self._minElements = []
        

    def push(self, val: int) -> None:
        if len(self._minElements) == 0 or self._minElements[-1] >= val:
            self._minElements.append(val)
        self._stack.append(val)

    def pop(self) -> None:
        val = self._stack.pop()
        if val == self.getMin():
            self._minElements.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._minElements[-1]
