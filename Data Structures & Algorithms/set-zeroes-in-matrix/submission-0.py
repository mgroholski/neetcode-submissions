'''
Algorithm:
Find all 0s, add row to rowsSet and columns to columnSet
Go through again and change

'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        columns = set()

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    rows.add(i)
                    columns.add(j)


        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in columns:
                    matrix[i][j] = 0