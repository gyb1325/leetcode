class Solution1:

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        self.helper(root, root.val, res)
        return sum(res)

    def helper(self, node, val, res):
        if not node.left and not node.right:
            res.append(val)
        if node.left:
            self.helper(node.left, val * 10 + node.left.val, res)
        if node.right:
            self.helper(node.right, val * 10 + node.right.val, res)


class Solution2:

    def sumNumbers(self, root):
        if not root:
            return 0
        sum_val = 0
        stack = [(root, root.val)]
        while stack:
            node, res = stack.pop()
            if not node.left and not node.right:
                sum_val += res
            if node.left:
                stack.append((node.left, res * 10 + node.left.val))
            if node.right:
                stack.append((node.right, res * 10 + node.right.val))
        return sum_val
