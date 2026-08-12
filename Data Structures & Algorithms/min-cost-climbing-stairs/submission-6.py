class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # memo to store seen
        memo = [-1]*len(cost)

        # dfs
        def dfs(i):
            # i too long -> return 0
            if i >= len(cost):
                return 0
            # if memo exist, return it
            if memo[i] != -1:
                return memo[i]
            # get memo = cost + min(dfs(i+2),dfs(i+1))
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]
        
        return min(dfs(0),dfs(1))