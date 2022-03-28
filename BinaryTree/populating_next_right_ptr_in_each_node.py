from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        queue = deque([root])
        while queue:
            size = len(queue)
            prev = None
            while size > 0:
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev = node
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
                size -= 1
        return root


if __name__ == '__main__':
    tc1 = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    tc2 = Node(1)
    ans = Solution().connect(root=tc2)
    print(ans)
