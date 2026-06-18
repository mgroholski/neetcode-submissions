# You are given an `n x n` matrix `grid` where each value `grid[i][j]` represents the elevation 
# at (i,j).

# The rain starts to fall. At time `t`, the depth of the water everywhere is `t`. You can swim from
# a square to another 4-directionally adjcent square iff the elevation of boths quares 
# indvidually are at most `t`. You can swim infinite distances in zero time.
# Of course, you must stay within the boundaries of the grid during your swim.

# Retun the least time until you can reach the bottom right square (n-1,n-1) 
# if you start at the top left square (0,0).


# Let current spot be (i, j)
# You can reach a in min((i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1))
import heapq

class Solution:
    def directions(self):
        return [(-1,0), (1,0),(0,-1),(0,1)]

    def swimInWater(self, grid: List[List[int]]) -> int:
        dp = [[float('inf')] * len(grid) for _ in range(len(grid))]
        dp[-1][-1] = grid[-1][-1]


        startPoint = (len(grid) - 1, len(grid) - 1)
        seenSet = set()
        heap = []
        heapq.heappush(heap, (dp[-1][-1], startPoint))
        seenSet.add(startPoint)
        
        while len(heap) > 0:
            _, currentPoint = heapq.heappop(heap)
            i,j = currentPoint
            for iDelta, jDelta in self.directions():
                if 0 <= (i + iDelta) < len(grid) and 0 <= (j + jDelta) < len(grid):
                    newPoint = (i + iDelta, j + jDelta)
                    if not newPoint in seenSet:
                        dp[i + iDelta][j + jDelta] = max(grid[i + iDelta][j + jDelta], dp[i][j])
                        heapq.heappush(heap, (dp[i + iDelta][j + jDelta], newPoint))
                        seenSet.add(newPoint)

        return dp[0][0]

        