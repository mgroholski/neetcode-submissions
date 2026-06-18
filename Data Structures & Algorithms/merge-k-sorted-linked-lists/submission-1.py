# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def mergeLists(self, l1, l2):
        head = point = None

        while l1 and l2:
            if l1.val <= l2.val:
                if not head:
                    head = point = l1
                else:
                    point.next = l1
                    point = point.next
                l1 = l1.next
            else:
                if not head:
                    head = point = l2
                else:
                    point.next = l2
                    point = point.next
                l2 = l2.next

        if not l1:
            if not head:
                head = point = l2
            else:
                point.next = l2
        else:
            if not head:
                head = point = l1
            else:
                point.next = l1

        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        amount = len(lists)
        interval = 1

        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.mergeLists(lists[i], lists[i + interval])
            interval *= 2
            
        return lists[0] if len(lists) else None

