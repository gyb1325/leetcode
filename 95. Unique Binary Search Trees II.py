# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper([i for i in range(1, n + 1)])

    def helper(self, lst):
        if not lst:
            return [None]
        res = []
        for i in range(len(lst)):
            for left in self.helper(lst[:i]):
                for right in self.helper(lst[i + 1:]):
                    node, node.left, node.right = TreeNode(lst[i]), left, right
                    res += [node]
        return res
