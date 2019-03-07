# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        f1 = None
        f2 = None
        flag = True
        res = None
        stack = []
        original = root
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            if res:
                if node.val < res.val and flag:
                    f1 = res
                    f2 = node  # Corner Case, two adjacent element swap
                    flag = False
                elif node.val < res.val and not flag:
                    f2 = node
                    break
            res = node
            root = node.right
        f1.val, f2.val = f2.val, f1.val
