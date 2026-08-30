class Solution:
    def numSquares(self, n: int) -> int:
        #dp[i] = least# of perfect sq num that sum to i
        dp = [n] *(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            #1, 2 .., n
            #transition
            for s in range(1, i+1):
                square = s*s
                if square > i:
                    break
                # try from i - square to i 
                dp[i] = min(dp[i], dp[i-square]+1)
        return dp[n]