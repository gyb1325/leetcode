"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dic = {}
        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)
            dic[ptr] = new_node
            ptr = ptr.next
        ptr = head
        while ptr:
            temp_node = dic[ptr]
            if ptr.next != None:
                temp_node.next = dic[ptr.next]
            if ptr.random != None:
                temp_node.random = dic[ptr.random]
            ptr = ptr.next
        return dic[head]
