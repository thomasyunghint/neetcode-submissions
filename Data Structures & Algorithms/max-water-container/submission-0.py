class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0, len(heights)-1
        area_max=0

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            if l<r and heights[l] < heights[r]:
                l+=1
            elif l<r and heights[l] >= heights[r]:
                r-=1
            area_max = max(area_max, area)
        return area_max
