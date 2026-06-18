# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = None
        currentNode = None

        while len(lists):
            lists.sort(key = lambda node: node.val)
            lowestNode = lists.pop(0)
            if lowestNode.next:
                lists.append(lowestNode.next)
            lowestNode.next = None
            if not root:
                root = lowestNode
                currentNode = root
            else:
                currentNode.next = lowestNode
                currentNode = lowestNode
            
        return root


