class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text2), len(text1)
        dp = [[0]*(n+1) for _ in range(m+1)]
        #dp[r][c] = longestCommonSubsequence from r,c to bottom right
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if text1[c] == text2[r]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        return dp[0][0]