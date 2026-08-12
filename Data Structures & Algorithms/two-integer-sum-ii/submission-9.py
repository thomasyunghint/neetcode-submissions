class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l,r= 0,len(n)-1

        while l<r:
            cur=n[l]+n[r]

            if cur>target:
                r-=1
            elif cur<target:
                l+=1
            else:
                return [l+1, r+1]
        return []