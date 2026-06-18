# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head
        prevNode = None

        while n:
            nextNode = n.next
            n.next = prevNode
            prevNode = n
            n = nextNode

        return prevNode