'''
Two dp arrays

atlantic and pacific

pacific
[[1,1,1,1,1],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]

atlantic
[[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[1,1,1,1,1]]

We can BFS until a 1 is reached

'''


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        
        pacific = [[0 for _ in range(n)] for _ in range(m)]
        atlantic = [[0 for _ in range(n)] for _ in range(m)]

        pacificQueue = []
        atlanticQueue = []

        for i in range(n):
            pacificQueue.append((0,i))
            atlanticQueue.append((m-1,i))

        for j in range(m):
            pacificQueue.append((j,0))
            atlanticQueue.append((j,n - 1))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while pacificQueue:
            x,y = pacificQueue.pop(0)
            if pacific[x][y] != 1:
                pacific[x][y] = 1
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and heights[x][y] <= heights[nx][ny]:
                        pacificQueue.append((nx, ny))

        while atlanticQueue:
            x,y = atlanticQueue.pop(0)
            if atlantic[x][y] != 1:
                atlantic[x][y] = 1
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and heights[x][y] <= heights[nx][ny]:
                        atlanticQueue.append((nx, ny))

        res = []
        for i, row in enumerate(heights):
            for j, _ in enumerate(row):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i,j])
        return res
        