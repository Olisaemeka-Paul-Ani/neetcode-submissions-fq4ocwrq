class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=output =0
        j = len(heights)-1
        while i < j:
            currWater = (j-i)*min(heights[i],heights[j])
            output = max(output,currWater)
            
            if heights[i] < heights[j]:
                i=i+1
            else:
                j=j-1
        return output