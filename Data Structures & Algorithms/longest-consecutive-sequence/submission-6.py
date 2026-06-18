class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)
        
        for i in numSet:
            if not i - 1 in numSet:
                curNum = i
                sol = 1
                while curNum + 1 in numSet:
                    sol += 1
                    curNum += 1
                res = max(sol, res)

        return res


                    

