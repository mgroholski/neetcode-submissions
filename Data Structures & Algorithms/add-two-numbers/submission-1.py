# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        head = None
        currentNode = None

        while l1 and l2:
            nodeSum = l1.val + l2.val + carry
            carry = int(nodeSum > 9)
            
            newNode = ListNode(nodeSum % 10)
            if not head:
                head = newNode
                currentNode = newNode
            else:
                currentNode.next = newNode

            currentNode = newNode
            l1 = l1.next
            l2 = l2.next

        while l1:
            nodeSum = l1.val + carry
            carry = int(nodeSum > 9)
            newNode = ListNode(nodeSum % 10)
            currentNode.next = newNode

            currentNode = newNode
            l1 = l1.next
        
        while l2:
            nodeSum = l2.val + carry
            carry = int(nodeSum > 9)
            newNode = ListNode(nodeSum % 10)
            currentNode.next = newNode

            currentNode = newNode
            l2 = l2.next

        if carry:
            newNode = ListNode(1)
            currentNode.next = newNode

        return head




        