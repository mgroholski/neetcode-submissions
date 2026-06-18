# cost = [1,2,3]

# Base Case
# i == 0 or i == 1 -> cost[i]

# Let idx be the current idx
# calculatedCost = min(calculatedCost[i - 1], calculatedCost[i - 2])


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        calculatedCost = [0] * (len(cost) + 1)

        for idx in range(len(cost) + 1):
            if idx > 1:
                calculatedCost[idx] = min(calculatedCost[idx - 1] + cost[idx - 1], calculatedCost[idx - 2] + cost[idx - 2])

        return calculatedCost[-1]
        