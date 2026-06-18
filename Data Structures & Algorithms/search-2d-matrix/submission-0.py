class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
                return False
        n = len(matrix[0])


        left = 0
        right  = m * n - 1
        while left <= right:
                mid = int((right - left) / 2 + left)
                val = matrix[mid // n][mid % n]
                if val == target:
                        return True
                elif val > target:
                        right = mid - 1
                else:
                        left = mid + 1

        return False
        