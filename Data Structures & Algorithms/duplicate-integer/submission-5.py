class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i=0
        while i <len(nums):
            if i == len(nums)-1:
                break
            else:
                if nums[i] == nums[i+1]:
                    return True
            i = i+1
        return False