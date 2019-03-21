# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        ptr = head
        length = 1
        while ptr.next != None:
            ptr = ptr.next
            length += 1

        r_number = k % length
        if k == 0 or r_number == 0:
            return head

        fast_ptr = head
        slow_ptr = head
        for _ in range(r_number):
            fast_ptr = fast_ptr.next

        while fast_ptr.next != None:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next

        temp = slow_ptr.next
        fast_ptr.next = head
        slow_ptr.next = None
        head = temp
        return head
