class Solution:
    def climbStairs(self, n: int) -> int:
        #state dp[i] = number of distinct ways to reach i-th  stair
        dp = [0]*(n+1)
        #base case on the ground dp[0] = 1 (no need to climbf)
        #or dp[1] = 1 (climb 1 step to 1st floor)
        dp[0], dp[1] = 1, 1
        #then use for loop to get through all cases in dp (transition)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        #then return dp (input n since the state definition of dp[i] is how many steps to climb to i-th stair)
        #last step either from dp's i-1 or i-2
        return dp[n]