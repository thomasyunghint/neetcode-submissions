class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows set 0 to 9
        rows = [set() for i in range(9)]
        # cols set 0 to 9
        cols = [set() for i in range(9)]
        # squares set 0to3 in 0to3
        sqs = [[set() for i in range(3)] for i in range(3)]
        #sqs[r//3][c//3]
        # loop r in range(9):
        for r in range(9):
            # loop c in range(9):
            for c in range(9):
                #if board[r][c] == ".":
                    #continue
                if board[r][c] == ".":
                    continue
                # if board[r][c] in rows set/ cols set / square set:
                    #return False
                if (board[r][c] in rows[r] or board[r][c] in cols[c]
                    or board[r][c] in sqs[r//3][c//3]):
                    return False
                # rows[r] add board[r][c]
                rows[r].add(board[r][c])
                # cols[c] add  board[r][c]
                cols[c].add(board[r][c])
                # square[square_key] add board[r][c]
                sqs[r//3][c//3].add(board[r][c])
        #return true
        return True