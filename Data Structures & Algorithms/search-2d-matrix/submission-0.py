class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][len(matrix[0]) - 1]:
                row = i

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
            