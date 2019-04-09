# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = dummy = ListNode(0)
        dummy.next = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        half = slow.next
        slow.next = None
        half = self.reverseList(half)
        while half:
            if half.val != head.val:
                return False
            half = half.next
            head = head.next
        return True

    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        return prev
