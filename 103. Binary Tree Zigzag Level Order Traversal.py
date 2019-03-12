# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append((root, 0))
        while q:
            temp, level = q.popleft()
            if level % 2 == 0:
                if len(res) - 1 == level:
                    res[level].insert(0, temp.val)
                else:
                    res.append([temp.val])
            else:
                if len(res) - 1 == level:
                    res[level].append(temp.val)
                else:
                    res.append([temp.val])
            if temp.right:
                q.append((temp.right, level + 1))
            if temp.left:
                q.append((temp.left, level + 1))
        return res
