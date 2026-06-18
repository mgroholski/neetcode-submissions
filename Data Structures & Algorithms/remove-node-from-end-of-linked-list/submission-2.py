# Start moving nToLastNode after currentNode has moved n times


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        trailingPreviousNode = None
        trailingNode = head
        currentNode = head
        
        passedNodes = 1

        while currentNode:
            currentNode = currentNode.next
            if passedNodes > n:
                trailingPreviousNode = trailingNode
                trailingNode = trailingNode.next
            passedNodes += 1

        if trailingNode.next:
            if not trailingPreviousNode:
                head = trailingNode.next
            else:
                trailingPreviousNode.next = trailingNode.next
        elif trailingPreviousNode:
            trailingPreviousNode.next = None
        else:
            head = None
        return head
        