class Solution:
    def dfs(self, root, reachable, grid):
        DIRECTIONS = set([(1,0), (-1,0), (0,1), (0,-1)])

        stack = [root]
        reachable.add(root)
        while len(stack):
            i,j = stack.pop()
            
            for direction in DIRECTIONS:
                newI, newJ = direction[0] + i, direction[1] + j
                newCoordinates = (newI, newJ)
                if 0 <= newI < len(grid) and 0 <= newJ < len(grid[0]):
                    if grid[newI][newJ] >= grid[i][j] and newCoordinates not in reachable:
                        reachable.add(newCoordinates)
                        stack.append(newCoordinates)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificReachable = set()
        atlanticReachable = set()
        
        for i in range(max(len(heights), len(heights[0]))):
            # Pacific upper and atlantic bottom
            if 0 <= i < len(heights[0]):
                self.dfs((0,i), pacificReachable, heights)
                self.dfs((len(heights) - 1, i), atlanticReachable, heights)

            # Pacific left and atlantic right
            if 0 <= i < len(heights):
                self.dfs((i,0), pacificReachable, heights)
                self.dfs((i, len(heights[0]) - 1), atlanticReachable, heights)

        return [list(x) for x in pacificReachable.intersection(atlanticReachable)]