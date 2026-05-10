class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        i=0
        while i < len(nums):
            output = output^nums[i]
            i=i+1
        return output
        