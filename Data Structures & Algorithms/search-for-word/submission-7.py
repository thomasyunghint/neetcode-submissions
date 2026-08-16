class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, i):
            # good found it -> True
            if i == len(word):        
                return True
            # bad: out of bound, not same char -> False
            if (r<0 or c<0 or r>=ROWS or c>=COLS or board[r][c] != word[i]):
                return False
            #store cell temporarily
            temp = board[r][c]
            board[r][c] = "#"
            #explore diff directions
            res =  (dfs(r+1,c,i+1) or
                    dfs(r-1,c,i+1) or
                    dfs(r,c+1,i+1) or
                    dfs(r,c-1,i+1))
            #restore cell
            board[r][c] = temp
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False