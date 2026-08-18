class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #multi source BFS
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        def bfs(r,c):
            #out of bound or water or in visit already -> return
            if (r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == -1 or (r,c) in visit):
                return
            visit.add((r,c))
            q.append([r,c])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()            
                grid[r][c] = dist
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            dist+=1