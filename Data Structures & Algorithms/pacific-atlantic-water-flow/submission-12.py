from _heapq import heapify
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res=[]

        def dfs(r,c, visit, prevHeight):
            # if out of bound -> return
            if ((r,c) in visit or 
                min(r,c) < 0 or 
                r == ROWS or c == COLS or 
                 heights[r][c] < prevHeight):
                 return
            #put in visit -> try other 4 directions
            visit.add((r,c))
            dfs(r+1,c, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])
        #loop c
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        #loop r
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        #loop r and c
        for r in range(ROWS):
            for c in range(COLS):
                #if in pac & atl at the same time -> res add
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
