# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        dummy = prev = ListNode(0)
        dummy.next = head
        cur = head
        while cur:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next
