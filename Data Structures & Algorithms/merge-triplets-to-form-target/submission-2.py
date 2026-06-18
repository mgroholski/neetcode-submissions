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
        possibleTriplets = [[], [], []]
        for triplet in triplets:
            matchIdx = set()
            for i in range(3):
                if triplet[i] == target[i]:
                    matchIdx.add(i)

            goodTriplet = True
            for i in range(3):
                if i not in matchIdx:
                    if triplet[i] > target[i]:
                        goodTriplet = False
                        break

            if not goodTriplet:
                continue

            for i in matchIdx:
                possibleTriplets[i].append(triplet)

        for l in possibleTriplets:
            if not len(l):
                return False

        return True