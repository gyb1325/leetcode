# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        res = [float("-inf")]
        self.max_down(root, res)
        return res[0]

    def max_down(self, root, res):
        if not root:
            return 0
        left = max(0, self.max_down(root.left, res))
        right = max(0, self.max_down(root.right, res))
        res[0] = max(res[0], root.val + left + right)
        return root.val + max(left, right)
