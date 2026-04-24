class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l=0
        r = len(matrix[0])-1
        while l<r:
            top = l
            bottom =r
            for i in range(r-l):
                topLeft=matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l]=matrix[bottom][r-i]
                matrix[bottom][r-i]= matrix[top+i][r]
                matrix[top+i][r]= topLeft
            l=l+1
            r=r-1
            
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        