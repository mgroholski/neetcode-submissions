'''
Binary search problem

if target is outside bounds 
    return false

How to convert a 1d index to 2d index?
i = idx // n
j = idx - (i * n)


'''


class Solution:
    def getVal(self,matrix, idx):
        m, n = len(matrix), len(matrix[0])
        i = idx // n
        j = idx - (i * n)
        return matrix[i][j]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n) - 1
        while l <= r:
            mid = (r + l) // 2
            val = self.getVal(matrix, mid)

            if target == val:
                return True
            elif target < val:
                r = mid - 1
            else:
                l = mid + 1
        return False