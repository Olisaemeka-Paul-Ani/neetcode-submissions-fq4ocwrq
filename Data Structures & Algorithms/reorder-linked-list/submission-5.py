# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return
        slow=head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = head
        secondHalf = 0
        
        while curr:
            if curr.next == slow:
                secondHalf = curr.next
                curr.next = None
                break
            curr=curr.next
            
        prev = None
        curr= secondHalf
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        secondHalf = prev
            
        currOne = head
        currTwo = secondHalf
        
        while currOne:
            nextOne = currOne.next
            nextTwo = currTwo.next
            
            currOne.next = currTwo
            currTwo.next = nextOne
            
            currOne = nextOne
            currTwo = nextTwo
        if currTwo:
            curr=head
            while curr:
                if curr.next==None:
                    curr.next=currTwo
                    break
                curr = curr.next
                
        