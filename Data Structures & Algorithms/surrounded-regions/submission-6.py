class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m,n = len(board),len(board[0])
        
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        seenSet = set()
        for i in range(m):
            for j in range(n):
                val = board[i][j]
                
                if val == 'O' and (i,j) not in seenSet:
                    curSet = set()
                    edge = False

                    queue = [(i,j)]
                    while queue:
                        u = queue.pop(0)
                        if u not in curSet:
                            curSet.add(u)
                            x,y = u
                            if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                                edge = True
                            for dx, dy in dirs:
                                nx, ny = dx + x, dy + y
                                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                                    queue.append((nx,ny))

                    if not edge:
                        for x,y in curSet:
                            board[x][y] = 'X'

                    seenSet = seenSet.union(curSet)
