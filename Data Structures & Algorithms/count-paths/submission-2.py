class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0
        dp = [1]*n
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + dp[j]
            dp = newRow
        return dp[0]