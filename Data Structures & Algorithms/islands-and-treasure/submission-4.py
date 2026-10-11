class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # since we want to guarantee shortest path use bfs

        # to optimize we run bfs only from treasures and mark
        # each land node as we visit them

        ROWS, COLS = len(grid), len(grid[0])

        INF = 2147483647

        queue = collections.deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append([i,j])
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while queue:
            curr = queue.popleft()
            row = curr[0]
            col = curr[1]

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and grid[nr][nc] == INF
                ):
                    grid[nr][nc] = grid[row][col] + 1
                    queue.append((nr, nc))



            

        




                        

