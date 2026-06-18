class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2:
            return False

        halfSum = totalSum // 2
        sumSet = set([0])

        for i in range(len(nums) - 1, -1, -1):
            if halfSum in sumSet:
                return True

            newSet = set()
            for s in sumSet:
                newSet.add(s + nums[i])
            sumSet = sumSet.union(newSet)

        return halfSum in sumSet

