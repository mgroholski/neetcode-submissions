import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        while l < r:
            mid = (l + r) // 2
            hourSpent = 0

            for pile in piles:
                hourSpent += math.ceil(pile / mid)
            
            if hourSpent <= h:
                r = mid
            else:
                l = mid + 1
            
        return r

