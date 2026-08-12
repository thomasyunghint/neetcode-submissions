class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            #all subsets that includes nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            #all subsets that do not includes nums[i]
            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1, subset)
        backtrack(0,[])
        return res