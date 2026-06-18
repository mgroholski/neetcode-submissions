class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.sol = set()

        def permute(curSol, numSet):
            if not len(numSet):
                self.sol.add(tuple(curSol))
                return

            for i in numSet.copy():
                numSet.remove(i)
                permute(curSol + [i], numSet)
                numSet.add(i)
            
        permute([], set(nums))
        return sorted([list(i) for i in self.sol])
        