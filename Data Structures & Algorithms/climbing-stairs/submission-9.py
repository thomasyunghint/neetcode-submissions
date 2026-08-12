class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        # n <=2 return it
        if n <=2:
            return n
        dp[1], dp[2] = 1,2
        # for i in range(1, n+1):
        for i in range(3,n+1):
            # dp i = sum first 2 steps
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        