# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.append(root)
        total_num = 0
        while q:
            node = q.popleft()
            total_num += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return total_num


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.get_Depth(root.left)
        right_depth = self.get_Depth(root.right)
        if left_depth == right_depth:
            return 2**left_depth + self.countNodes(root.right)
        else:
            return 2**right_depth + self.countNodes(root.left)

    def get_Depth(self, node):
        if not node:
            return 0
        else:
            return 1 + self.get_Depth(node.left)
