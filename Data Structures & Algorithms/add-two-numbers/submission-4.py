# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head = ListNode()
        s = sum_head
        l1_h, l2_h = l1, l2

        carry = 0
        while l1_h and l2_h:
            n_val = l1_h.val + l2_h.val + carry
            carry = 0
            if n_val > 9:
                carry = n_val // 10
                n_val %= 10

            s.next = ListNode(n_val)
            s = s.next
            l1_h = l1_h.next
            l2_h = l2_h.next

        while l1_h:
            n_val = l1_h.val + carry
            carry = 0
            if n_val > 9:
                carry = n_val // 10
                n_val %= 10

            s.next = ListNode(n_val)
            s = s.next
            l1_h = l1_h.next

        while l2_h:
            n_val = l2_h.val + carry
            carry = 0
            if n_val > 9:
                carry = n_val // 10
                n_val %= 10

            s.next = ListNode(n_val)
            s = s.next
            l2_h = l2_h.next

        if carry > 0:
            n_val = carry
            s.next = ListNode(n_val)
            s = s.next

        return sum_head.next
        