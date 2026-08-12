class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # store each ans
        memo = [-1]*len(cost)
        # dfs
        def dfs(i):
            # i too long -> 0
            if i >= len(cost):
                return 0
            # if exist already
            if memo[i] != -1:
                return memo[i]
            # recursive
            memo[i] = cost[i] + min(dfs(i+1),dfs(i+2))
            # return memo
            return memo[i]
        
        return min(dfs(0),dfs(1))