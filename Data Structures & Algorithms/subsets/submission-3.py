class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur = []
        def dfs(i, cur):
            #basecase: if i >= nums length -> add copy to res 
            if i >= len(nums):
                res.append(cur.copy())
                return
            #dfs(i+1) for nums[i] case
            cur.append(nums[i])
            dfs(i+1, cur)

            #pop it out then dfs(i+1)
            cur.pop()
            dfs(i+1, cur)

        dfs(0, [])
        return res