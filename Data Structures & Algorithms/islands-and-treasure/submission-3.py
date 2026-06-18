class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        rooms = grid
        m,n = len(rooms), len(rooms[0])

        queue = []
        for i, row in enumerate(rooms):
            for j, val in enumerate(row):
                if not val:
                    queue.append((0,(i,j)))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        seenSet = set()
        while queue:
            dist, (x,y) = queue.pop(0)

            if (x,y) not in seenSet:
                seenSet.add((x,y))
                rooms[x][y] = dist
                for (dx, dy) in directions:
                    nx, ny = dx + x, dy + y

                    if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == 2147483647:
                        queue.append((dist + 1, (nx,ny)))
        









            


        