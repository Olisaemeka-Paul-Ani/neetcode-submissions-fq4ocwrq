class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        clone = nums[:]
        nums.sort()
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i]+nums[j]== target:
                output = []
                output.append(clone.index(nums[i]))
                clone[clone.index(nums[i])]="x"
                output.append(clone.index(nums[j]))
                output.sort()
                return output
            elif nums[i]+nums[j] < target:
                i = i+1
            elif nums[i]+nums[j] > target:
                j = j-1
            
        