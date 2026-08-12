class Solution:
    def numDecodings(self, s: str) -> int:
        #memoization so base case
        dp = {len(s): 1}

        #dfs
        def dfs(i):
            #if in: return
            if i in dp:
                return dp[i] 
            #if 0: return 0
            if s[i] == "0":
                return 0
            #1-digit case
            res = dfs(i+1)
            #2-digit case
            if i+1<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")) :
                res += dfs(i+2)
            #save in dp hashmap
            dp[i] = res
            return res
        
        #return largest problem
        return dfs(0)