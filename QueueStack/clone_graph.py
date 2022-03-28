from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        my_graph = {node: Node(node.val)}
        stack = deque([node])
        while stack:
            n = stack.pop()
            for neigh in n.neighbors:
                if neigh not in my_graph:
                    my_graph[neigh] = Node(neigh.val)
                    stack.append(neigh)
                my_graph[n].neighbors.append(my_graph[neigh])
        return my_graph[node]


if __name__ == '__main__':
    print(Solution().cloneGraph())

