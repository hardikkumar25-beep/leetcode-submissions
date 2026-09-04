class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        max_area=0
        while l<r:
            length=min(height[l],height[r])
            width=r-l
            area=length*width
            if area>max_area:
                max_area=area
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
        