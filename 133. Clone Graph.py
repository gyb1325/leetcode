"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        # DFS
        # stack = [node]
        # new_node = Node(node.val, [])
        # dic = {node: new_node}
        # while stack:
        #     temp = stack.pop()
        #     for n in temp.neighbors:
        #         if n not in dic:
        #             neighborcopy = Node(n.val, [])
        #             dic[n] = neighborcopy
        #             dic[temp].neighbors.append(neighborcopy)
        #             stack.append(n)
        #         else:
        #             dic[temp].neighbors.append(dic[n])
        # return new_node
        # BFS
        queue = collections.deque()
        queue.append(node)
        new_node = Node(node.val, [])
        dic = {node: new_node}
        while queue:
            temp = queue.popleft()
            for n in temp.neighbors:
                if n not in dic:
                    new_neighbors = Node(n.val, [])
                    dic[n] = new_neighbors
                    dic[temp].neighbors.append(new_neighbors)
                    queue.append(n)
                else:
                    dic[temp].neighbors.append(dic[n])
        return new_node
