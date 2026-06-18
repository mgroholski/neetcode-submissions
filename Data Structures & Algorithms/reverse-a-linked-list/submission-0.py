# Use stack to reverse direction
# Set head to last node
# currentNode = stack.pop()
# stack.top().next -> currentNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        currentNode = head
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previous
            previous = currentNode
            currentNode = nextNode
        head = previous
        return head
        
        