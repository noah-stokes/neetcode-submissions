class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # since we want to guarantee shortest path use bfs

        # to optimize we run bfs only from treasures and mark
        # each land node as we visit them

        ROWS, COLS = len(grid), len(grid[0])

        INF = 2147483647

        visited = set()

        queue = collections.deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append([i,j,0])
        
        while queue:
            curr = queue.popleft()
            row = curr[0]
            col = curr[1]
            depth = curr[2]

            if ((row,col) in visited) or (grid[row][col] == -1):
                continue
            
            visited.add((row,col))

            if grid[row][col] == INF:
                grid[row][col] = depth
            
            if row + 1 < ROWS:
                queue.append([row+1,col,depth+1])
            if row - 1 >= 0:
                queue.append([row-1,col,depth+1])
            if col + 1 < COLS:
                queue.append([row,col+1,depth+1])
            if col - 1 >= 0:
                queue.append([row,col-1,depth+1])
            

            

        




                        

