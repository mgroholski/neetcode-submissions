class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = []
        colSets = []
        squareSets = []
        squareSetsRow = []
        for _ in range(len(board)):
            rowSets.append(set(range(1,10)))
            colSets.append(set(range(1,10)))
            squareSetsRow.append(set(range(1,10)))
            if len(squareSetsRow) == 3:
                squareSets.append(squareSetsRow)
                squareSetsRow = []

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val != ".":
                    val = int(val)
                    if (val in rowSets[i]) and (val in colSets[j]) and (val in squareSets[i // 3][j // 3]):
                        rowSets[i].remove(val)
                        colSets[j].remove(val)
                        squareSets[i // 3][j // 3].remove(val)
                    else:
                        return False
        return True