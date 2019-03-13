# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # if inorder:
        #     idx = inorder.index(postorder.pop())
        #     root = TreeNode(inorder[idx])
        #     root.right = self.buildTree(inorder[idx+1:], postorder)
        #     root.left = self.buildTree(inorder[:idx], postorder)
        #     return root
        if not inorder:
            return None
        idx = {}
        for i, v in enumerate(inorder):
            idx[v] = i
        root = TreeNode(postorder[-1])
        stack = [root]
        for val in postorder[-2::-1]:
            node = TreeNode(val)
            if idx[val] > idx[stack[-1].val]:
                stack[-1].right = node
            else:
                while stack and idx[val] < idx[stack[-1].val]:
                    n = stack.pop()
                n.left = node
            stack.append(node)
        return root
