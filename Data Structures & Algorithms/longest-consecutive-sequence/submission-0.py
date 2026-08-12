class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #edge case
        if not nums: return 0
        #set
        num_set = set(nums)
        #longest=0
        longest=0
        #for n in set?
        for n in num_set:
            # if n-1 not in set():
            if (n-1) not in num_set:
                #curr_num=n 
                curr_num = n
                #curr_streak=1
                curr_streak=1
                #when curr_num+1 in set():
                while (curr_num+1) in num_set:
                    #curr_num += 1
                    #curr_streak +=1
                    curr_num+=1
                    curr_streak+=1
                #longest = max(longest, curr_streak)
                longest = max(longest, curr_streak)
        #return longest
        return longest