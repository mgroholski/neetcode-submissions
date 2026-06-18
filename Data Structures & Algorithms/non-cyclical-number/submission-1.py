class Solution:
    def isHappy(self, n: int) -> bool:
        
        seenSet = set()
        def dfs(n):
            nonlocal seenSet
            if n in seenSet:
                return False
            elif n == 1:
                return True

            seenSet.add(n)
            new_n = 0
            for i in str(n):
                new_n += int(i) ** 2

            return dfs(new_n)

        return dfs(n)

        

        