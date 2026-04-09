class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        bottom = row-1
        while top <=bottom:
            mid = (top+bottom)//2
            if target < matrix[mid][0]:
                bottom = mid-1
            elif target > matrix[mid][-1]:
                top = mid+1
            else:
                break
        if not(top <= bottom):
            return False
                    
        i = 0
        j = col-1
        
        while i <= j:
            middle = (i+j)//2
            if target == matrix[mid][middle]:
                return True
            elif target < matrix[mid][middle]:
                j= middle-1
            else:
                i=middle+1
        return False


            