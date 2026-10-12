class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and (i,j) not in visited:
                    region = set()

                    queue = collections.deque([[i,j]])
                    visited.add((i,j))
                    region.add((i,j))

                    surrounded = True

                    while queue:
                        r, c = queue.popleft()

                        if r == ROWS - 1 or r == 0 or c == COLS - 1 or c == 0:
                            surrounded = False

                        if r + 1 < ROWS and (r+1,c) not in visited and board[r+1][c] == 'O':
                            queue.append([r+1,c])
                            visited.add((r+1,c))
                            region.add((r+1,c))
                        if r - 1 >= 0 and (r-1,c) not in visited and board[r-1][c] == 'O':
                            queue.append([r-1,c])
                            visited.add((r-1,c))
                            region.add((r-1,c))
                        if c + 1 < COLS and (r,c+1) not in visited and board[r][c+1] == 'O':
                            queue.append([r,c+1])
                            visited.add((r,c+1))
                            region.add((r,c+1))
                        if c - 1 >= 0 and (r,c-1) not in visited and board[r][c-1] == 'O':
                            queue.append([r,c-1])
                            visited.add((r,c-1))
                            region.add((r,c-1))
                    
                    if surrounded:
                        for x, y in region:
                            board[x][y] = 'X'
                        
                        
                        




                        
