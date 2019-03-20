# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, h1, h2):
        dummy = ptr = ListNode(0)
        while h1 and h2:
            if h1.val < h2.val:
                ptr.next, ptr, h1 = h1, h1, h1.next
            else:
                ptr.next, ptr, h2 = h2, h2, h2.next
        ptr.next = h1 or h2
        return dummy.next
