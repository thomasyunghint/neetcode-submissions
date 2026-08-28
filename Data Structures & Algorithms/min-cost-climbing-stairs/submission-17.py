class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp[i]: the minimum cost to reach i-th stair
        dp = [0] * (len(cost)+1)
        dp[0], dp[1] = 0, 0
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[len(cost)]