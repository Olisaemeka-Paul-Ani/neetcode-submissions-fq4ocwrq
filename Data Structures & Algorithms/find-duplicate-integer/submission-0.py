class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        isTrue = True

        while isTrue:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                isTrue = False
        slowPtr = 0
        isTrue = True

        while isTrue:
            slow = nums[slow]
            slowPtr = nums[slowPtr]
            if slowPtr == slow:
                isTrue = False
        return slow
        