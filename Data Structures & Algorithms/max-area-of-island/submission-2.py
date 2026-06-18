class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        res = 0
        seenSet = set()

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if (i,j) not in seenSet and val == 1:
                    area = 0
                    stack = [(i,j)]
                    while stack:
                        x,y = stack.pop()
                        if (x,y) not in seenSet:
                            seenSet.add((x,y))
                            area += 1

                            for dx, dy in directions:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                                    stack.append((nx, ny))
                    res = max(res, area)
        return res
        