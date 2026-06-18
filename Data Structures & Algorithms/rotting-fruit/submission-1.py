class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        rottenQueue = []
        orangeCnt = 0
        rottenCnt = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    rottenQueue.append((0, (i,j)))
                    rottenCnt += 1
                elif val == 1:
                    orangeCnt += 1

        res = 0
        seenSet = set()
        while rottenQueue:
            t, (x,y) = rottenQueue.pop(0)

            if (x,y) not in seenSet:
                seenSet.add((x,y))
                res = max(res, t)

                for dx, dy in directions:
                    nx, ny = dx + x, dy +y
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        rottenQueue.append((t + 1, (nx, ny)))

        if len(seenSet) - rottenCnt == orangeCnt:
            return res
        else:
            return -1
                        




        