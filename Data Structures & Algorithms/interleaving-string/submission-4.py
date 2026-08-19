class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #base -> if length diff -> False
        if len(s1) + len(s2) != len(s3):
            return False
        #dp + dfs memo since many sub problems
        dp = {}
        #i,j
        def dfs(i, j):
            # if both reach end
            if i == len(s1) and j == len(s2):
                return True 
            # if in dp
            if (i,j) in dp:
                return dp[(i,j)]
            # if i good: in bound and same char and can do dfs
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1,j):
                return True
            # if j good
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i,j+1):
                return True
            #bad store in dp; return
            dp[(i,j)] = False
            return False

        return dfs(0,0)
            