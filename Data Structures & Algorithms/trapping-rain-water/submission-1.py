'''
Algorithm

leftPointer = 0
rightPointer = end

maxLeft, maxRight = respective starting heights
water = 0

while rightPointer != leftPointer:
    move left + 1 if <= right
        maxLeft = max(maxRight, height[left])
        water += max(0, min(maxLeft, maxRight) - height[left])
    else move right - 1
        maxRight = max(maxRight, height[right])
        water += max(0, min(maxLeft, maxRight) - height[right])
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1

        maxLeft, maxRight = height[l], height[r]
        water = 0

        while l != r:
            newHeight = 0
            if height[l] <= height[r]:
                l += 1
                newHeight = height[l]
                maxLeft = max(maxLeft, newHeight)
            else:
                r -= 1
                newHeight = height[r]
                maxRight = max(maxRight, newHeight)

            water += max(0, min(maxLeft, maxRight) - newHeight)
        
        return water
                

        