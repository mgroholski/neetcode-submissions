class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for i, target in enumerate(nums):
            seenSet = set()

            for j in range(i + 1, len(nums)):
                diff = -1 * (target + nums[j])

                if diff in seenSet:
                    res.add(tuple(sorted([target, nums[j], diff])))
                seenSet.add(nums[j])

        return [list(i) for i in res]
        