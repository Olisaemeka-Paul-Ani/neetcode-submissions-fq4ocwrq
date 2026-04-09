class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = ["*"]*len(nums)
        suffix =  ["*"]*len(nums)
        product = 1
        i = 0
        while i < len(nums):
            if i == 0:
                prefix[i] =product
                i = i+1
            else:
                product = product * nums[i-1]
                prefix[i]= product
                i = i+1
        i,product = len(suffix)-1,1
        while i >=0:
            if i == len(suffix)-1: 
                suffix[i]=product
                i = i-1
            else:
                product = product * nums[i+1]
                suffix[i] = product
                i = i-1
        i = 0
        while i < len(nums):
            nums[i] = suffix[i]*prefix[i]
            i = i+1
        return nums

