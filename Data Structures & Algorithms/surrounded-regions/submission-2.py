class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # multisource bfs from border
        ROWS = len(board)
        COLS = len(board[0])

        queue = collections.deque()

        for c in range(COLS):
            if board[0][c] == 'O':
                queue.append([0,c])
                board[0][c] = 'T'
            if board[ROWS-1][c] == 'O':
                queue.append([ROWS-1,c])
                board[ROWS-1][c] = 'T'

        for r in range(ROWS):
            if board[r][0] == 'O':
                queue.append([r,0])
                board[r][0] = 'T'
            if board[r][COLS-1] == 'O':
                queue.append([r,COLS-1])
                board[r][COLS-1] = 'T'

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    board[nr][nc] == 'O'
                ):
                    queue.append([nr,nc])
                    board[nr][nc] = 'T'

        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
 
            
            
            

        

    
                        
                        




                        
