class Solution:
    def directions(self):
        return set([(1,0), (-1,0), (0,1), (0,-1)])

    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshFruitCount = 0
        
        queue = []
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    queue.append(((i,j), 0))
                elif val == 1:
                    freshFruitCount += 1

        seenSet = set([x[0] for x in queue])
        maxDistance = 0
        while len(queue):
            coordinates, distance = queue.pop(0)
            i, j = coordinates

            maxDistance = max(distance, maxDistance)
            for direction in self.directions():
                nextI, nextJ = i + direction[0], j + direction[1]
                nextCoordinates = (nextI, nextJ)
                if 0 <= nextI < len(grid) and 0 <= nextJ < len(grid[0]):
                    if nextCoordinates not in seenSet and grid[nextI][nextJ] == 1:
                        queue.append((nextCoordinates, distance + 1))
                        seenSet.add(nextCoordinates)
                        freshFruitCount -= 1
        
        return maxDistance if freshFruitCount == 0 else -1