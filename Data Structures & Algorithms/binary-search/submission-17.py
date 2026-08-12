class Solution:
    def search(self, n: List[int], target: int) -> int:
        l,r=0,len(n)-1

        while l<=r:
            m=(l+r)//2

            if n[m] == target:
                return m
            elif n[m] < target:
                l=m+1
            else:
                r=m-1
        return -1