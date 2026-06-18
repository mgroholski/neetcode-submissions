class Solution:
    def solve(self, board: List[List[str]]) -> None:
        DIRECTIONS = set([(1,0), (-1,0), (0,1), (0,-1)])

        seenSet = set()
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                coordinates = (i,j)
                if val == 'O' and coordinates not in seenSet:
                    queue = [coordinates]
                    group = set([coordinates])

                    surrounded = True
                    while len(queue):
                        m,n = queue.pop(0)
                        if m == 0 or m == len(board) - 1:
                            surrounded = False
                        elif n == 0 or n == len(board[0]) - 1:
                            surrounded = False
                        
                        for direction in DIRECTIONS:
                            newI, newJ = direction[0] + m, direction[1] + n
                            newCoordinates = (newI, newJ)
                            if 0 <= newI < len(board) and 0 <= newJ < len(board[0]):
                                if board[newI][newJ] == 'O' and newCoordinates not in group:
                                    queue.append(newCoordinates)
                                    group.add(newCoordinates)

                    if surrounded:
                        for m,n in group:
                            board[m][n] = 'X'
                    else:
                        seenSet = seenSet.union(group)
                        print(seenSet)



        