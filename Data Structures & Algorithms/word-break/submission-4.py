class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False]*(len(s)+1)
        #basecase 
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                # if enough space + verbatim->dp can jump
                if i+len(w)<= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                # if true already -> break 
                if dp[i]:
                    break
            
        return dp[0]