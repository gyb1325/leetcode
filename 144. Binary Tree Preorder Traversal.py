# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Method 1
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            if temp:
                res.append(temp.val)
                stack.append(temp.right)
                stack.append(temp.left)
        return res
        # Method 2
        # stack = []
        # res = []
        # p = root
        # while stack or p:
        #     if p:
        #         stack.append(p)
        #         res.append(p.val)
        #         p = p.left
        #     else:
        #         node =stack.pop()
        #         p = node.right
        # return res
