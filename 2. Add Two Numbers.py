# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ptr = ListNode(0)
        while l1 and l2:
            node = ListNode((carry + l1.val + l2.val) % 10)
            carry = (carry + l1.val + l2.val) // 10
            ptr.next = node
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            node = ListNode((carry + l1.val) % 10)
            carry = (carry + l1.val) // 10
            ptr.next = node
            ptr = ptr.next
            l1 = l1.next
        while l2:
            node = ListNode((carry + l2.val) % 10)
            carry = (carry + l2.val) // 10
            ptr.next = node
            ptr = ptr.next
            l2 = l2.next
        while carry:
            node = ListNode(carry)
            ptr.next = node
            ptr = ptr.next
            carry = 0

        return dummy.next
