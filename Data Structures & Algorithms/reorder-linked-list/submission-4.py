# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Reverse latter half of list

'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 

        # Get middleptr and lastPtr
        middleTrailPtr = None
        middlePtr, lastPtr = head, head
        while lastPtr.next and lastPtr.next.next:
            lastPtr = lastPtr.next.next
            middleTrailPtr = middlePtr
            middlePtr = middlePtr.next
        
        if middlePtr == lastPtr:
            return 

        if lastPtr.next:
            middleTrailPtr = middlePtr
            middlePtr = middlePtr.next
            lastPtr = lastPtr.next

        middleTrailPtr.next = None

        # Reverse from middlePtr on 
        hPtr = None
        while middlePtr:
            nextPtr = middlePtr.next
            middlePtr.next = hPtr
            hPtr = middlePtr
            middlePtr = nextPtr

        # Combine from head and lastPtr
        headPtr = head
        while headPtr and lastPtr:
            nHeadPtr = headPtr.next
            nLastPtr = lastPtr.next

            headPtr.next = lastPtr
            if nHeadPtr:
                lastPtr.next = nHeadPtr

            headPtr = nHeadPtr
            lastPtr = nLastPtr 
        return