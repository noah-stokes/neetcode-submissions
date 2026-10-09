class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterative bfs
        islands = 0
        stack = collections.deque()

        for ri in range(len(grid)):
            for ci in range(len(grid[0])):
                if grid[ri][ci] == "1":
                    stack.append([ri,ci])
                    islands += 1

                    while stack:
                        curr = stack.popleft()
                        r = curr[0]
                        c = curr[1]

                        if r < 0 or r >= len(grid):
                            continue
                        if c < 0 or c >= len(grid[0]):
                            continue
                        if grid[r][c] == "0":
                            continue 
                        
                        
                        grid[r][c] = "0"

                        stack.append([r-1, c])
                        stack.append([r+1, c])
                        stack.append([r, c-1])
                        stack.append([r, c+1])          

        return islands


