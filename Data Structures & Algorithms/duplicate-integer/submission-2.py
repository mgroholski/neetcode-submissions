class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenSet = set()

        for n in nums:
            if n in seenSet:
                return True
            seenSet.add(n)
        return False

         