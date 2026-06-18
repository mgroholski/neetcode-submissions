'''
We are trying to create target from the triplets list. We can only use the max values from within the triplet list.


triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]

[2,5,3] -> ([1,7,5]) [2,7,5]

Brute force - Enumeration
We can try every set of triplets to determine if the target is created

Optimized
1. Create three lists with the values we need in each position.
2. Remove any triplet that changes the max
3. If all lists have at least one value left, return true
'''

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = (0,0,0)

        for triplet in triplets:
            lessThanOrEqualTo = (triplet[0] <= target[0] 
            and triplet[1] <= target[1]
            and triplet[2] <= target[2]
            )

            if lessThanOrEqualTo:
                res = (
                    max(res[0], triplet[0]), 
                    max(res[1], triplet[1]), 
                    max(res[2], triplet[2])
                )

        return res == tuple(target)