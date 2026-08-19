class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        def dfs(i,j):
            #if both reach end -> good
            if i == len(s1) and j == len(s2):
                return True
            # if in -> return itself
            if (i,j) in dp:
                return dp[(i,j)]
            # if i good: in bound, s1 and s3 same char, can do dfs -> T
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1,j):
                return True
            # if j good: in bound, s2 and s3 same char, can do dfs -> T
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i,j+1):
                return True
            # bad, save in dp; return
            dp[(i,j)] = False
            return False
        return dfs(0,0)