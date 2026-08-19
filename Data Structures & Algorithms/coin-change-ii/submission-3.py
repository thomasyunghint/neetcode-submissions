class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1) #use dp to save calculated result; 1d for space
        dp[0]=1 #only 1 method if $0 diff

        for i in range(len(coins)-1, -1, -1):
        #reverse calculation
            for a in range(1, amount+1):
                #if this required amount can be filled completely or partially by this coin
                if coins[i] <= a:
                    dp[a] += dp[a-coins[i]]
        return dp[amount]