class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        meow = [amount+1]*(amount+1)
        #define dp[k] = min numbers of coin to reach $k
        #$0 needs 0 coin
        meow[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if a >= c:
                    meow[a] = min(meow[a], 1 + meow[a-c])
        return -1 if meow[amount] == (amount+1) else meow[amount]
