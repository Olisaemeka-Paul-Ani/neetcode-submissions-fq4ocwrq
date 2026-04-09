class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack =[]
        for i,j in enumerate(heights):
            start = i
            while stack and stack[-1][1] > j:
                start = i
                pastWidth, pastHeight = stack.pop()
                maxArea = max(maxArea, (pastHeight * (start-pastWidth)))
                start = pastWidth
            stack.append([start,j])


        for i, j in stack:
            maxArea = max(maxArea, j* (len(heights)-i))
        return maxArea
        


        