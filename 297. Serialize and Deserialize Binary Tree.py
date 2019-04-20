# The above only applies no dupilicates case

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "+"
        pre_list = self.preorder(root)
        in_list = self.inorder(root)
        a1 = " ".join(pre_list)
        a2 = " ".join(in_list)
        s = a1 + "+" + a2
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "+":
            return None
        total = data.split("+")
        pre_list = total[0].split(" ")
        in_list = total[1].split(" ")
        root = self.construct_tree(pre_list, in_list)
        return root

    def construct_tree(self, pre_ord, in_ord):
        if in_ord:
            idx = in_ord.index(pre_ord.pop(0))
            root = TreeNode(int(in_ord[idx]))
            root.left = self.construct_tree(pre_ord, in_ord[:idx])
            root.right = self.construct_tree(pre_ord, in_ord[idx + 1:])
            return root

    def preorder(self, root):
        if not root:
            return []
        return [str(root.val)] + self.preorder(root.left) + self.preorder(root.right)

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [str(root.val)] + self.inorder(root.right)

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        lst = []
        self.pre_order(root, lst)
        s = " ".join(lst)
        print(s)
        return s

    def pre_order(self, root, lst):
        if not root:
            lst.append("#")
        else:
            lst.append(str(root.val))
            self.pre_order(root.left, lst)
            self.pre_order(root.right, lst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        new_data = data.split(" ")
        root = self.recover(new_data)
        return root

    def recover(self, data):
        temp = data.pop(0)
        if temp == "#":
            return None
        else:
            node = TreeNode(int(temp))
            node.left = self.recover(data)
            node.right = self.recover(data)
            return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
