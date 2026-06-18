class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenSet = set()
        for i in nums:
            if i in seenSet:
                return True
            else:
                seenSet.add(i)

        return False