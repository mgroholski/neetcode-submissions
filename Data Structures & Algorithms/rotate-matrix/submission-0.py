class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        lastIdx = n - 1

        # Reflect over y = -x
        for i in range(n):
            for j in range(i, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        # Reflect over vertical
        for i in range(n):
            for j in range(n // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][lastIdx - j]
                matrix[i][lastIdx - j] = tmp
    



        
        


        

        