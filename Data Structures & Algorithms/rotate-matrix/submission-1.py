'''

'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix), len(matrix[0])

        tmp = []
        for i in range(m):
            newRow = []
            for j in range(n-1, -1, -1):
                newRow.append(matrix[j][i])
            tmp.append(newRow)

        for i, row in enumerate(tmp):
            for j, val in enumerate(row):
                matrix[i][j] = val