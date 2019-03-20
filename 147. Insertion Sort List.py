# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev_ptr = head
        ptr = head.next
        while ptr:
            move_flag = False
            prev_pivot = dummy
            pivot = dummy.next
            while pivot is not ptr:
                if ptr.val < pivot.val:
                    prev_ptr.next = ptr.next
                    prev_pivot.next = ptr
                    ptr.next = pivot
                    move_flag = True
                    break
                else:
                    pivot, prev_pivot = pivot.next, pivot
            if move_flag:
                ptr = prev_ptr.next
            else:
                ptr, prev_ptr = ptr.next, ptr
        return dummy.next
