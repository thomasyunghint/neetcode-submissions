class Solution:
    def integerBreak(self, n: int) -> int:
        #memoization
        #base
        dp = {1:1}
        #all case
        for num in range(2, n+1):
            # update dp[num] an illegal num if ==n then itself, else num
            dp[num] = 0 if num==n else num
            #loop all case!
            for i in range(1, num):
                #get product
                val = dp[i]*dp[num-i]
                #update dp[num]
                dp[num] = max(dp[num], val)
        return dp[n]