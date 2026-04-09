class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j= len(nums)-1
        output = float("inf")
        while i <=j:
            if nums[i] < nums[j]:
                output=min(output,nums[i])
                break
            m = (i+j)//2

            if nums[i] <= nums[m]:
                output=min(output,nums[m])
                i=m+1
            else:
                output=min(output,nums[m])
                j=m-1
        return output




                
        

        