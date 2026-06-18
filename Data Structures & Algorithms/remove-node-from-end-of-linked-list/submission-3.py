# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
            We want a trailing pointer that is n + 1 nodes back. So that when we reach the end of the list we can move the next.

            We need to consider the edge cases that if there is no next next (n = 1) or the trailingPtr is still at the head node
        '''

        if not head:
            return None

        n += 1
        curNode = head
        trailingPtr = head

        while curNode:
            if n <= 0:
                trailingPtr = trailingPtr.next
            curNode = curNode.next
            n -= 1

        if n == 0:
            trailingPtr.next = trailingPtr.next.next
        else:
            if trailingPtr == head:
                head = head.next
            elif trailingPtr.next and trailingPtr.next.next:
                trailingPtr.next = trailingPtr.next.next
            elif trailingPtr.next and not trailingPtr.next.next:
                trailingPtr.next = None

        return head

        
