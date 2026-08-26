class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()
        l = 0
        for r in range(len(nums)):
            #if gap too large -> shorten window (remove element and l+=1)
            if r - l > k:
                win.remove(nums[l])
                l+=1
            #if in
            if nums[r] in win:
                return True
            win.add(nums[r])
        return False