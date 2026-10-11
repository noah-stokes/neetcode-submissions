class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0

        queue = collections.deque()

        ROWS, COLS = len(grid), len(grid[0])

        fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append([nr,nc])
            minutes += 1
        
        return minutes if fresh == 0 else -1
            
            

