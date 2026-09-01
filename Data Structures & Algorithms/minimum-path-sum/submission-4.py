class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #dp r,c : minimal sum of all numbers from r,c to bottom right
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        dp[m][n-1] = 0
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r][c+1], dp[r+1][c])
        return dp[0][0]