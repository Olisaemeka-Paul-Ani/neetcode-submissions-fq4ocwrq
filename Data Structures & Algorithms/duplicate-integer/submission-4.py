class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i =0
        j=i+1
        while i<len(nums):
            while j< len(nums):
                if nums[j]==nums[i]:
                    return True
                else:
                    j=j+1
            i=i+1
            j=i+1
        return False