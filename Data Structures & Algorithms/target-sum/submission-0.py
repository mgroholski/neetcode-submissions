import functools

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.cache = {}
        self.nums = nums

        def backtrack(idx, target) -> int:
            if (idx, target) in self.cache:
                return self.cache[(idx, target)]

            if idx == len(self.nums):
                result = 1 if not target else 0
                if not (idx, target) in self.cache:
                    self.cache[(idx, target)] = result
                return result
            
            count = 0
            currentElement = self.nums[idx]
            count += backtrack(idx + 1, target + currentElement)
            count += backtrack(idx + 1, target - currentElement)

            self.cache[(idx, target)] = count
            return count

        return backtrack(0, target)
