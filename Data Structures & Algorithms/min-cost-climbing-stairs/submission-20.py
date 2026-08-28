class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp[i] means that the minimum cost to reach i-th stair
        dp = [0]*(len(cost)+1)
        dp[0], dp[1] = 0, 0
        # for 2 to n
        for i in range(2, len(cost)+1):
            #dpi = dp[i-1] + i-1 to i, dp[i-2] + i-2 to i
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[len(cost)]