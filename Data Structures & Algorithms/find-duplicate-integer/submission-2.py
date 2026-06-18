# Slow pointer, fast pointer

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowIdx, fastIdx = 0,0

        while slowIdx == 0 or slowIdx != fastIdx:
            # One jump
            slowIdx = nums[slowIdx]

            # Two jump
            nextFastIdx = nums[fastIdx]
            fastIdx = nums[nextFastIdx]

        startIdx = 0
        while slowIdx != startIdx:
            slowIdx = nums[slowIdx]
            startIdx = nums[startIdx]
        
        return startIdx


        