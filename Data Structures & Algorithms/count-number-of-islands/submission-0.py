# if x not in seenSet:
#   count += 1
#   run BFS to get MST


class Solution:
    def directions(self):
        return [(1,0), (-1,0), (0,1), (0,-1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        seenSet = set()

        for i, row in enumerate(grid):
            for j, val in enumerate(grid[i]):
                currentCoordinate = (i,j)
                if val == "1" and currentCoordinate not in seenSet:
                    count += 1
                    queue = [currentCoordinate]

                    while len(queue):
                        coordinate = queue.pop(0)
                        for direction in self.directions():
                            nextCoordinate = (coordinate[0] + direction[0], coordinate[1] + direction[1])
                            if 0 <= nextCoordinate[0] < len(grid) and 0 <= nextCoordinate[1] < len(grid[0]):
                                if grid[nextCoordinate[0]][nextCoordinate[1]] == "1" and nextCoordinate not in seenSet:
                                    queue.append(nextCoordinate)
                                    seenSet.add(nextCoordinate)

        return count





        