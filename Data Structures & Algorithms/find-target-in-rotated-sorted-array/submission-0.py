class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while i <j:
            if nums[i] < nums[j]:
                break
            m = (i+j)//2
            if nums[i] <= nums[m]:
                i=m+1
            else:
                j=m
                
        m=i
        i=0
        j= len(nums)-1
        
        if nums[m]== target:
            return m
        if target > nums[m] and target <= nums[j]:
            l = m
            r= len(nums)-1
            while l <= r:
                m = (l+r)//2
                if nums[m]== target:
                    return m
                elif target > nums[m]:
                    l=m+1
                else:
                    r=m-1
            return -1
        else:
            r=m
            l=0
            while l <= r:
                m = (l+r)//2
                if nums[m]== target:
                    return m
                elif target > nums[m]:
                    l=m+1
                else:
                    r=m-1
            return -1