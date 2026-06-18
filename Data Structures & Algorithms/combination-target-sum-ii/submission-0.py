class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.solSet = set()

        def backtrack(sol, target, candidates):
            if target == 0:
                self.solSet.add(tuple(sorted(list(sol))))
                return
            elif target < 0:
                return

            seenSet = set()
            for i, val in enumerate(candidates):
                if val not in seenSet:
                    candidates.pop(i)
                    backtrack(tuple(list(sol) + [val]), target - val, candidates)
                    candidates.insert(i, val)
                    seenSet.add(val)

        backtrack((), target, candidates)
        return [list(x) for x in self.solSet]

