'''
Each time we switch, we'll add a bound that direction

bounds = [0,0,0,0]
directions = [(0,1), (1,0), (0,-1), (-1,0)]

idx = 0

'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        
        idx = 0
        bounds = [0, 0, 0, 1]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        x,y = 0,0
        res = []
        while len(res) < m*n:
            # print(x,y, idx, bounds, directions[idx], res)
            res.append(matrix[x][y])

            dx, dy = directions[idx]
            bound = bounds[idx]

            switch = False
            if dx >= 0 and dy >= 0:
                if dx > 0 and x == (m - 1 - bound):
                    switch = True
                elif dy > 0 and y == (n - 1 - bound):
                    switch = True
            else:
                if dx < 0 and x == bound:
                    switch = True
                elif dy < 0 and y == bound:
                    switch = True

            if switch:
                bounds[idx] += 1
                idx = (idx + 1) % 4
                dx, dy = directions[idx]
                bound = bounds[idx]                    
            x, y = x + dx, y + dy

        return res
        