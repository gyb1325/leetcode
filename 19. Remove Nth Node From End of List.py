# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        ptr1 = head
        ptr2 = head
        for _ in range(n - 1):
            ptr2 = ptr2.next
        while ptr2.next is not None:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
            prev = prev.next
        prev.next = ptr1.next
        return dummy.next
