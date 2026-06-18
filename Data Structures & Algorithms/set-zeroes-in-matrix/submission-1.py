class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowIdx = set()
        colIdx = set()

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if not val:
                    rowIdx.add(i)
                    colIdx.add(j)


        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if i in rowIdx or j in colIdx:
                    matrix[i][j] = 0
        