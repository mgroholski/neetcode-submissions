class Solution:
    def trap(self, height: List[int]) -> int:
        trappedWater = 0
        i = 0
        while i < len(height) and height[i] == 0:
            i += 1
        
        while i < len(height) - 1:
            j = i + 1

            maxHeight = 0
            maxHeightIndex = j
            while j < len(height) and height[i] > height[j]:
                if height[j] >= maxHeight:
                    maxHeight = height[j]
                    maxHeightIndex = j
                j += 1
            
            # Calculates current trapped water
            minHeight = 0
            if j == len(height):
                minHeight = min(height[i], maxHeight)
            else:
                minHeight = min(height[i], height[j])
                maxHeightIndex = j

            currentTrappedWater = 0
            for k in range(i + 1, maxHeightIndex):
                currentTrappedWater += max(minHeight - height[k], 0)
            
            trappedWater += currentTrappedWater
            i = maxHeightIndex
        return trappedWater
        