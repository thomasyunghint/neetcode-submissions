class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r = 0, len(h)-1
        max_area=0
        area=0

        while l < r:
            area = min(h[l],h[r]) * (r-l)
            max_area = max(max_area, area)

            if h[l] <= h[r]:
                l+=1
            else:
                r-=1
        return max_area