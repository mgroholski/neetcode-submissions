# Get middle node
# Reverse second half of list
# Merge two lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        previousNode = None
        list2Node = head
        currentNode = head
        move = True

        while currentNode.next:
            currentNode = currentNode.next
            if move:
                previousNode = list2Node
                list2Node = list2Node.next
            move = not move

        previousNode.next = None
        previousNode = None
        while list2Node:
            nextNode = list2Node.next
            list2Node.next = previousNode
            previousNode = list2Node
            list2Node = nextNode
        
        list2Node = previousNode
        list1Node = head
        while list1Node and list2Node:
            l1Current = list1Node
            l2Current = list2Node

            list1Node = list1Node.next
            list2Node = list2Node.next

            l1Current.next = l2Current
            if list1Node:
                l2Current.next = list1Node
            else:
                l2Current.next = list2Node
            

        


        



        