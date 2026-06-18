# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []

        currentNode = head
        lastEndNode = None
        while currentNode:
            stack.append(currentNode)
            currentNode = currentNode.next

            if len(stack) == k:
                while len(stack):
                    node = stack.pop()
                    if not lastEndNode:
                        head = node
                    else:
                        lastEndNode.next = node
                    lastEndNode = node

        # Unload stack as a queue
        while len(stack):
            node = stack.pop(0)
            if not lastEndNode:
                head = node
            else:
                lastEndNode.next = node
            lastEndNode = node

        lastEndNode.next = None
        return head