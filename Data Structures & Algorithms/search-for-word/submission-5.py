# Base Case
#   length of word = 0 
# Check (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1) for next word letter



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(coordinates, word) -> bool:
            if not len(word):
                return True
            
            directions = [(1, 0), (-1, 0), (0, 1), (0,-1)]
            nextLetter, word = word[0], word[1:]
            lastCoordinate = coordinates[-1]

            for i, j in directions:
                newCoordinate = (lastCoordinate[0] + i, lastCoordinate[1] + j)
                if 0 <= newCoordinate[0] < len(board) and 0 <= newCoordinate[1] < len(board[0]) and newCoordinate not in coordinates:
                    if board[newCoordinate[0]][newCoordinate[1]] == nextLetter:
                        if backtrack(coordinates + [newCoordinate], word):
                            return True
            return False

        firstLetter, word = word[0], word[1:]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == firstLetter:
                    if backtrack([(i,j)], word):
                        return True

        return False