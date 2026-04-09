# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        random = ListNode
        dummy = random
        while curr:
            length = length+1
            curr = curr.next
        prev = dummy
        curr = head
        while length != n:
            length = length-1
            prev.next = curr
            curr = curr.next
            prev = prev.next


        prev.next = curr.next
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next

        return dummy.next

        