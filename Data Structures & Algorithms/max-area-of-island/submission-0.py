class Solution:
    def directions(self):
        return set([(1,0), (-1,0), (0,1), (0,-1)])

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        seenSet = set()

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                currentCoordinates = (i,j)
                if currentCoordinates not in seenSet and val == 1:
                    area = 0
                    queue = [currentCoordinates]
                    seenSet.add(currentCoordinates)

                    while len(queue):
                        coordinates = queue.pop(0)
                        area += 1

                        for direction in self.directions():
                            nextCoordinate = (coordinates[0] + direction[0], coordinates[1] + direction[1])
                            if 0 <= nextCoordinate[0] < len(grid) and 0 <= nextCoordinate[1] < len(grid[0]):
                                if nextCoordinate not in seenSet and grid[nextCoordinate[0]][nextCoordinate[1]] == 1:
                                    queue.append(nextCoordinate)
                                    seenSet.add(nextCoordinate)
                    maxArea = max(area, maxArea)
        return maxArea

        