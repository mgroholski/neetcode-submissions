class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        offset = []

        total = 0

        for g, c in zip(gas,cost):
            currentOffset = g - c
            offset.append(currentOffset)
            total += currentOffset

        maxDifferenceIdx = 0
        maxDifference = 0
        for i in range(len(offset)):
            difference = offset[i] - offset[(i - 1) % len(offset)]
            if difference > maxDifference:
                maxDifferenceIdx = i
                maxDifference = difference
                

        return -1 if total < 0 else maxDifferenceIdx
