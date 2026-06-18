class Solution:
    def directions(self):
        return set([(1,0), (-1,0), (0,-1), (0,1)])


    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                currentCoordinates = (i,j)
                if val == 0:
                    queue = [(currentCoordinates, 0)]
                    seenSet = set([currentCoordinates])

                    while len(queue):
                        coordinates, distance = queue.pop(0)
                        grid[coordinates[0]][coordinates[1]] = min(distance, grid[coordinates[0]][coordinates[1]])

                        for direction in self.directions():
                            nextCoordinates = (coordinates[0] + direction[0], coordinates[1] + direction[1])
                            if 0 <= nextCoordinates[0] < len(grid) and 0 <= nextCoordinates[1] < len(grid[0]):
                                if nextCoordinates not in seenSet and grid[nextCoordinates[0]][nextCoordinates[1]] != -1:
                                    queue.append((nextCoordinates, distance + 1))
                                    seenSet.add(nextCoordinates)

        