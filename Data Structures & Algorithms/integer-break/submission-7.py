class Solution:
    def integerBreak(self, n: int) -> int:
        #memoization
        dp = {1:1}
        #get all cases
        for num in range(2, n+1):
            dp[num] = 0 if num==n else num
            for i in range(1, num):
                val = dp[i]*dp[num-i]
                #update its largest
                dp[num] = max(dp[num], val)
        return dp[n]