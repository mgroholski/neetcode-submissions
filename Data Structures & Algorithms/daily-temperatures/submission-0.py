class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)

        for i, val in enumerate(temperatures):
            while len(stack) > 0 and val > temperatures[stack[-1]]:
                tempIdx = stack.pop()
                results[tempIdx] = i - tempIdx
            stack.append(i)
        return results
            


