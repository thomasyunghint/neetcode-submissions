class Solution:
    def numSquares(self, n: int) -> int:
        #dp
        dp = [n]*(n+1)
        #base
        dp[0] =0
        for target in range(1, n+1):
            #try all s within target
            for s in range(1, target+1):
                #get squares
                squares = s*s
                #if target - squares < 0
                if target - squares < 0:
                    break
                #update dp[target] 
                dp[target] = min(dp[target], 1+dp[target-squares])

        return dp[n]