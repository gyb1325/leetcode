# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Recursive method
        # if inorder:
        #     idx = inorder.index(preorder.pop(0))
        #     root = TreeNode(inorder[idx])
        #     root.left = self.buildTree(preorder, inorder[:idx])
        #     root.right = self.buildTree(preorder, inorder[idx+1:])
        #     return root
        # Iterative method
        if not preorder:
            return None
        idx = {}
        for i, v in enumerate(inorder):
            idx[v] = i
        root = TreeNode(preorder[0])
        stack = [root]

        for val in preorder[1:]:
            node = TreeNode(val)
            if idx[val] < idx[stack[-1].val]:
                stack[-1].left = node
            else:
                while stack and idx[val] > idx[stack[-1].val]:
                    n = stack.pop()
                n.right = node
            stack.append(node)
        return root
