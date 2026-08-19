class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        #loop coin types
        for i in range(len(coins)-1,-1,-1):
            #each coin can redo inf times
            for a in range(1, amount+1):
                #if this coin <= amount
                if coins[i] <= a:
                    #curr dp sum smaller diff
                    dp[a] += dp[a-coins[i]]
        return dp[amount]