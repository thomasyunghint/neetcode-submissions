class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #return min number of ops -> dp
        # many sub problem -> dfs, memo
        dp = {} 
        def dfs(a, b):

            # if wor1 reach end -> return the rest of word2
            if a == len(word1):
                return len(word2) - b
            # vice versa
            if b == len(word2):
                return len(word1) - a
            if (a,b) in dp:
                return dp[(a,b)]
            # if same char -> move point moves
            if word1[a] == word2[b]:
                ans = dfs(a+1,b+1) 
            else:
                #insert -> move a only
                insert = dfs(a+1,b)
                #delete -> move b only
                delete = dfs(a,b+1)
                #repalce -> move both
                replace = dfs(a+1,b+1)
                # ops = 1 + min of these 3
                ans = 1+ min(insert,delete,replace)
            #save in dp and return
            dp[(a,b)] =ans
            return ans
        return dfs(0,0)