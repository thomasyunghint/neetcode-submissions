class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def Capture(r,c):
            if (min(r,c)<0 or r>=ROWS or c>=COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"
            Capture(r+1,c)
            Capture(r-1,c)
            Capture(r,c+1)
            Capture(r,c-1)
            return
        # unsurrounded O -> T
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and ((r == 0 or r == ROWS-1) or (c == 0 or c == COLS-1)):
                    Capture(r,c)
        # surrounded O -> X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # unsurrounded T -> O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"