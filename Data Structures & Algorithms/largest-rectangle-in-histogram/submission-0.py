class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = []
        idx = 0
        while idx < len(heights):
            currentHeight = heights[idx]

            lastIdx = idx
            while len(stack) and stack[-1][1] > currentHeight:
                lastIdx, height = stack.pop()
                area = (idx - lastIdx) * height
                maxArea = max(maxArea, area)
            stack.append((lastIdx, currentHeight))
            idx += 1

        while len(stack):
            lastIdx, height = stack.pop()
            area = (idx - lastIdx) * height
            maxArea = max(maxArea, area)

        return maxArea