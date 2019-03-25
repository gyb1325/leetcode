# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Interative solution, BFS


class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = [0]
        queue = collections.deque()
        queue.append((root, 0))
        level_flag = 0
        while queue:
            node, level = queue.popleft()
            if level == level_flag:
                res[level] = node.val
            else:
                level_flag = level
                res.append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return res


# Recursive Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, 1, res)
        return res

    def helper(self, node, level, res):
        if not node:
            return
        if level > len(res):
            res.append(node.val)
        if node.right:
            self.helper(node.right, level + 1, res)
        if node.left:
            self.helper(node.left, level + 1, res)
