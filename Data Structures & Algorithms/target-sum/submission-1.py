'''
This is an enumeration problem. We'll need to explore every possible outcome. 
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.cache = {}
        self.nums = nums

        def dfs(idx, target):
            if (idx, target) in self.cache:
                return self.cache[(idx, target)]

            if idx == len(self.nums):
                result = 1 if not target else 0
                if not (idx, target) in self.cache:
                    self.cache[(idx, target)] = result
                return result
                

            res = 0
            curNum = self.nums[idx]
            res += dfs(idx + 1, target - curNum)
            res += dfs(idx + 1, target + curNum)
            self.cache[(idx, target)] = res
            return res

        return dfs(0, target)