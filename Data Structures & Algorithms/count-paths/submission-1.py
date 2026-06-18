'''
We can use a dynamic programming approach since many paths will use the same squares. 

Starting from the finish we can compute the amount of unique routes from square (x,y) to the beginning 
with paths = paths[x + 1][y] + paths[x][y+1] since from that spot the robot can move down or right


The bottom and right row has only one path

'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            paths[i][n - 1] = 1

        for i in range(n):
            paths[m - 1][i] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                paths[i][j] = paths[i + 1][j] + paths[i][j + 1]

        return paths[0][0]
        