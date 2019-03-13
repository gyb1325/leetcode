# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # if not root:
        #     return []
        # q = collections.deque()
        # q.append((root, 0))
        # res = []
        # while q:
        #     temp, level = q.popleft()
        #     if len(res) - 1 == level:
        #         res[level].append(temp.val)
        #     else:
        #         res.append([temp.val])
        #     if temp.left:
        #         q.append((temp.left, level + 1))
        #     if temp.right:
        #         q.append((temp.right, level + 1))
        # return res

        if not root:
            return []
        q = [[root]]
        for level in q:
            res = []
            for node in level:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
            if res:
                q.append(res)
        return [[node.val for node in level] for level in q]
