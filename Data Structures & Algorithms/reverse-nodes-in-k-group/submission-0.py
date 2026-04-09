# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(link, k):
            while link and k > 0:
                link = link.next
                k=k-1
            return link

        dummy = ListNode(0,head)
        dummyNode = dummy

        while True:
            kth = getKth(dummyNode, k)
            if not kth:
                break
            groupNext = kth.next
            curr = dummyNode.next
            nxt = kth.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = nxt
                nxt = curr
                curr = tmp
            tmp = dummyNode.next
            dummyNode.next = kth
            dummyNode= tmp
        return dummy.next
        