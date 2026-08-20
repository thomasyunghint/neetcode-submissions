class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        
        
        def dfs(alice, i, m):
            # reach end
            if i == len(piles):
                return 0
            # if in dp alrdy
            if (alice, i, m) in dp:
                return dp[(alice, i, m)]
            # try all x
            total=0
            res = 0 if alice else float('inf')
            for x in range(1, 2*m + 1):
                #if out of bound -> break
                if i+x > len(piles):
                    break
                #if in bound total add this
                total += piles[i+x-1]
                # alice case
                if alice:
                    res = max(res, total + dfs(not alice, i+x, max(m,x)))
                # bob case
                else:
                    res = min(res, dfs(not alice, i+x, max(m,x)))
            # put in dp
            dp[(alice, i, m)] = res
            # return
            return dp[(alice, i, m)]
        #return base
        return dfs(True, 0, 1)