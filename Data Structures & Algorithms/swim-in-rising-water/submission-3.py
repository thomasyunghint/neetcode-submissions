class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        directions = [[0,1],[0,-1], [1,0], [-1,0]]
        minH = [[grid[0][0], 0, 0]]
        visit.add((0,0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N-1 and c == N-1:
                return t
            for dr, dc in directions:
                nR, nC = r+dr, c+dc
                if ((nR,nC) in visit or nR<0 or nC<0 or nR==N or nC==N):
                    continue
                visit.add((nR,nC))
                heapq.heappush(minH, [max(t, grid[nR][nC]), nR, nC])