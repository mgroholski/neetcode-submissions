class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = set()

        def dfs(s, nums):
            if not len(nums):
                nonlocal sol
                sol.add(tuple(s))
                return

            dfs(s + [nums[0]], nums[1:])
            dfs(s, nums[1:])

        dfs([], nums)
        return [list(s) for s in sol]
        