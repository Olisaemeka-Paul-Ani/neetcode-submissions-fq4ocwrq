# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        hashSet = set()
        while current is not None:
            if hex(id(current)) in hashSet:
                return True
            hashSet.add(hex(id(current)))
            current=current.next
        return False

        