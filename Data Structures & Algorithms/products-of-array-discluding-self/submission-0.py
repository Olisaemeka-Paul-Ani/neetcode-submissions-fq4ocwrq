class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        i = 0
        answer = []
        while i < len(nums):
            prefix= nums[0:i]
            suffix = nums[i+1:len(nums)]
            if i == 0:
                answer.append(math.prod(suffix))
            elif i == len(nums)-1:
                answer.append(math.prod(prefix))
            else:
                answer.append(math.prod(prefix)*math.prod(suffix))
            i = i+1
        return answer
            