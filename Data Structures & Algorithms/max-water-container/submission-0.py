class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L=0
        R=len(heights)-1
        max_area=0
        while L<R:
            current_area=(R-L)*min(heights[L],heights[R])# width * height # width is [R-L] to simply show the space in between the bars don't take up any space either
            max_area=max(max_area,current_area)
            if (heights[L]<heights[R]) and L<R:
                L+=1
            else: # handles both heights[R]<heights[L] and heights[R]==heights[L]
                R-=1
        return max_area
            
        