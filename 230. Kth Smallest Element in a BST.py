# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        a = self.traverse(root)
        return a[k - 1]

    def traverse(self, treenode):
        if not treenode:
            return []
        return self.traverse(treenode.left) + [treenode.val] + self.traverse(treenode.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        n = self.countNode(root.left)
        if n >= k:
            return self.kthSmallest(root.left, k)
        elif n + 1 < k:
            return self.kthSmallest(root.right, k - n - 1)
        return root.val

    def countNode(self, node):
        if not node:
            return 0
        return self.countNode(node.left) + self.countNode(node.right) + 1
