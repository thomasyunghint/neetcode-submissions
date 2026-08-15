class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #sort firs
        res = []
        nums.sort()
        #dfs: transmit i, cur and current total
        def dfs(i, cur, total):
            #base: if same -> append copy to res
            if total == target:
                res.append(cur.copy())
                return
            # loop every j 
            for j in range(i, len(nums)):
                # base: too long -> return
                if total + nums[j] > target:
                    return
                #try new
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                #pop
                cur.pop()
        dfs(0,[],0)
        return res