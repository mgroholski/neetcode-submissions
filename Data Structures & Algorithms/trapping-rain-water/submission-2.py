'''
We use a two pointer approach that begins at different ends. We can then consider:

Move the pointer pointing to the lower height. If we find a location with a lower height than the previus min, this place will be filled with water. 

Minheight never goes down

'''


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        
        l,r = 0, len(height) - 1
        minHeight = 0
        while l < r:
            minHeight = max(minHeight, min(height[l], height[r]))
            if height[l] < minHeight:
                res += minHeight - height[l]
            elif height[r] < minHeight:
                res += minHeight - height[r]

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
        