# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        a, b = self._splitList(head)
        b = self._reverseList(b)
        head = self._mergeList(a, b)

    def _splitList(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        return head, middle

    def _reverseList(self, head):
        prev = None
        cur = head
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        return prev

    def _mergeList(self, a, b):
        ptr = head = a
        a = a.next
        while b:
            ptr.next = b
            ptr = ptr.next
            b = b.next
            if a:
                a, b = b, a
        return head
