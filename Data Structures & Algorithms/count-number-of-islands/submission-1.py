class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])

        res = 0
        seenSet = set()

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == "1" and (i,j) not in seenSet:
                    res += 1
                    directions = [(0,1), (0,-1), (1,0), (-1,0)]
                    queue = [(i,j)]
                    while queue:
                        x,y = queue.pop(0)
                        if (x,y) not in seenSet:
                            seenSet.add((x,y))
                            for dx, dy in directions:
                                nx, ny = x+dx, y+dy
                                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                                    queue.append((nx, ny))
        return res

        