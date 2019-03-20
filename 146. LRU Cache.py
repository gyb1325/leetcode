class Node:

    def __init__(self, key, val):
        self.key = key
        self.v = val
        self.nxt = None
        self.prv = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.nxt = self.tail
        self.tail.prv = self.head
        self.dic = {}

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            return node.v

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.dic:
            self._remove(self.dic[key])
            self._add(node)
            self.dic[key] = node
        else:
            self._add(node)
            self.dic[key] = node
            if self.cap > 0:
                self.cap -= 1
            else:
                removed = self.head.nxt
                key = removed.key
                self._remove(removed)
                del self.dic[key]

    def _add(self, node):
        prv_node = self.tail.prv
        prv_node.nxt = node
        node.prv = prv_node
        node.nxt = self.tail
        self.tail.prv = node

    def _remove(self, node):
        prv_node = node.prv
        prv_node.nxt = node.nxt
        node.nxt.prv = prv_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
