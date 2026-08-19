class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}


        def dfs(i,j):
            #base if either reach end
            if i == len(word1):
                return len(word2)-j                
            if j == len(word2):
                return len(word1)-i 
            #if in dp already
            if (i,j) in dp:
                return dp[(i,j)]
            #if both match
            if word1[i] == word2[j]:
                ans = dfs(i+1, j+1)
            else:
                insert = dfs(i,j+1)
                delete = dfs(i+1, j)
                replace = dfs(i+1,j+1)
                ans = 1 + min(insert,delete, replace)
            dp[(i,j)] = ans
            return ans
            
        return dfs(0,0)

            
        