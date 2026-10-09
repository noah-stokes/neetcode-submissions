class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # iterative dfs
        max_area = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = 0
                    grid[r][c] = 0

                    queue = collections.deque([[r,c]])

                    while queue:
                        curr = queue.pop()
                        row = curr[0]
                        col = curr[1]

                        area += 1

                        if row - 1 >= 0 and grid[row-1][col] == 1:
                            queue.append([row - 1, col])
                            grid[row-1][col] = 0
                        if row + 1 < len(grid) and grid[row+1][col] == 1:
                            queue.append([row + 1, col])
                            grid[row+1][col] = 0
                        if col - 1 >= 0 and grid[row][col-1] == 1:
                            queue.append([row, col - 1])
                            grid[row][col-1] = 0
                        if col + 1 < len(grid[0]) and grid[row][col+1] == 1:
                            queue.append([row, col + 1])
                            grid[row][col+1] = 0
                    
                    if area > max_area:
                        max_area = area
        return max_area
