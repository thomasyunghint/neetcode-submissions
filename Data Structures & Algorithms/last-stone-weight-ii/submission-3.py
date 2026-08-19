class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        dp={}
        target = math.ceil(stoneSum/2)
        def dfs(i, total):
            # if long enough or  too heavy -> return diff
            if i == len(stones) or total >= target:
                return abs(total - (stoneSum - total))
            # if in dp already -> return
            if (i,total) in dp:
                return dp[(i,total)]
            #exllore have or not have stones[i]
            dp[(i,total)] = min(dfs(i+1,total), dfs(i+1,total+stones[i]))
            #return
            return dp[(i,total)]
        return dfs(0,0)