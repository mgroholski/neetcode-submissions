# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitSet = set()

        n = head
        while n:
            if n in visitSet:
                return True
            
            visitSet.add(n)
            n = n.next

        return False
        