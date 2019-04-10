# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        self.helper(root, "", res)
        return res

    def helper(self, node, path, res):
        if not node.left and not node.right:
            res.append(path + str(node.val))
            return
        if node.left:
            self.helper(node.left, path + str(node.val) + "->", res)
        if node.right:
            self.helper(node.right, path + str(node.val) + "->", res)
