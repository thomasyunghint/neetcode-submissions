class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multisource BFS
        ROWS, COLS = len(grid), len(grid[0])
        q=deque()
        fresh, time = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh > 0:
            #check current layer
            for _ in range(len(q)):
                r,c = q.popleft()
                #explore nei
                for dr, dc in dir:
                    row = r + dr
                    col = c + dc
                    if 0<= row < ROWS and 0<= col < COLS and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append([row,col])
                        fresh -= 1
            time +=1
        return time if fresh==0 else -1