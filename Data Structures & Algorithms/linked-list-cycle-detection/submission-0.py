# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        found = set()

        currentNode = head
        while currentNode:
            if currentNode.val in found:
                return True
            
            found.add(currentNode.val)
            currentNode = currentNode.next
        return False