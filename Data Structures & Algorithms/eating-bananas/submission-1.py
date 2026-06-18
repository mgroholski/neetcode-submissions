'''
Searching for the minimum rate.

piles = [3,6,7,11], h = 8

[3,6,7,11] 
l,r = 1,11

k = 6
[3,6,7,11] 


'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        while l < r:
            mid = (l + r)//2

            hoursNeeded = 0
            for i in piles:
                hoursNeeded += math.ceil(i / mid)
            if hoursNeeded > h:
                l = mid + 1
            elif hoursNeeded <= h:
                r = mid 
            

        return l
        