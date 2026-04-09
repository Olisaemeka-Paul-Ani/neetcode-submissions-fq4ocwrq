# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoSorted(listOne, listTwo):
            head = ListNode(0)
            dummy = head

            while listOne and listTwo:
                if listOne.val < listTwo.val:
                    dummy.next = listOne
                    listOne = listOne.next
                else:
                    dummy.next = listTwo
                    listTwo = listTwo.next
                dummy = dummy.next

            if listOne:
                dummy.next = listOne
            if listTwo:
                dummy.next = listTwo

            return head.next
        if not lists or len(lists)==0:
            return None
        mergedLists = []
        while len(lists)>1:
            i=0
            mergedLists = []
            while i < len(lists):
                firstList = lists[i] if i < len(lists) else None
                secondList = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(mergeTwoSorted(firstList, secondList))
                i=i+2
            lists = mergedLists
        return lists[0]
            

