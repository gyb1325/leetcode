# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.helper(root, sum, [], res)
        return res

    def helper(self, root, sum, path, res):
        if not root:
            return
        if not root.left and not root.right and sum - root.val == 0:
            path.append(root.val)
            res.append(path)
        else:
            self.helper(root.left, sum - root.val, path + [root.val], res)
            self.helper(root.right, sum - root.val, path + [root.val], res)

        # if not root:
        #     return []
        # if root.val-sum ==0 and root.left == None and root.right == None:
        #     return  [[root.val]]
        # tmp = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right,sum-root.val)
        # return [[root.val] + i for i in tmp]
