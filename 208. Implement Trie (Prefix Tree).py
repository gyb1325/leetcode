class TreeNode:

    def __init__(self):
        self.isWord = False
        self.child = collections.defaultdict(TreeNode)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for s in word:
            cur = cur.child[s]
        cur.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for s in word:
            cur = cur.child.get(s)
            if not cur:
                return False
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for s in prefix:
            cur = cur.child.get(s)
            if not cur:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
