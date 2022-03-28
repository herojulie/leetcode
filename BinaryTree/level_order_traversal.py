from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        answer: List[List[int]] = []
        queue = deque([root])

        while queue:
            size = len(queue)
            level_node = []
            while size > 0:
                node = queue.popleft()
                level_node.append(node.val)
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
                size -= 1
            answer.append(level_node)

        return answer


if __name__ == '__main__':
    tc1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    tc2 = TreeNode(1)
    tc3 = []

    s = Solution()
    print(s.levelOrder(root=tc3))
