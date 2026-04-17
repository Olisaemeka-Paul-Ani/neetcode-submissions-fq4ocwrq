class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        i=0
        j= len(height)-1
        maxLeft = height[i]
        maxRight = height[j]
        output = 0


        while i < j:
            if maxLeft < maxRight:
                i=i+1
                maxLeft = max(maxLeft, height[i])
                output = output + (maxLeft-height[i])
            else:
                j=j-1
                maxRight = max(maxRight, height[j])
                output = output+(maxRight-height[j])
        return output
        