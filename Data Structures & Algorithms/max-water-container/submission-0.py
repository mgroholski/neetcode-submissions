class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        maximumArea = 0

        while i < j:
            area = (j - i) * (min(heights[i], heights[j]))
            maximumArea = max(area, maximumArea)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maximumArea