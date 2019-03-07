# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    #     def isValidBST(self, root: TreeNode) -> bool:
    #         Min, Max = float("-inf"), float("inf")
    #         return self.helper(root, Min, Max)

    #     def helper(self, node, Min, Max):
    #         if not node: return True
    #         if not node.left and not node.right:
    #             if Min<node.val<Max:
    #                 return True
    #             else:
    #                 return False
    #         if node.left and not node.right:
    #             return self.helper(node.left, Min, node.val) and node.val > node.left.val
    #         elif node.right and not node.left:
    #             return self.helper(node.right, node.val, Max) and node.val < node.right.val

    #         else:
    #             return self.helper(node.right, node.val, Max) and self.helper(node.left, Min, node.val) and \
    #                     node.left.val < node.val < node.right.val

    def isValidBST(self, root: TreeNode) -> bool:
        res = float("-inf")
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return True
            node = stack.pop()
            if node.val <= res:
                return False
            res = node.val
            root = node.right
