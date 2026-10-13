class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        u = 0
        l = len(matrix) - 1

        while u <= l:
            m = (l + u) // 2
             
            if target < matrix[m][0]:
                l = m - 1
            elif target > matrix[m][-1]:
                u = m + 1
            else:
                row = m
                break

        if row == -1:
            return False
        
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
            
        return False
            