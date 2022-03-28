from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(l_node: TreeNode, r_node: TreeNode) -> bool:
            if l_node is None and r_node is None:
                return True
            if l_node is None or r_node is None:
                return False
            if l_node.val == r_node.val:
                return is_mirror(l_node.left, r_node.right) and is_mirror(l_node.right, r_node.left)
            else:
                return False
        return is_mirror(root.left, root.right)

    # iterative
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     if root.left is None and root.right is None:
    #         return True
    #     if (root.left and root.right is None) or (root.right and root.left is None):
    #         return False
    #
    #     l_queue = deque([root.left])
    #     r_queue = deque([root.right])
    #
    #     while l_queue and r_queue:
    #         l_node = l_queue.popleft()
    #         r_node = r_queue.popleft()
    #
    #         if l_node.val != r_node.val:
    #             return False
    #
    #         if (l_node.left and r_node.right is None) or (l_node.right and r_node.left is None):
    #             return False
    #
    #         l_queue.append(l_node.left) if l_node.left else None
    #         r_queue.append(r_node.right) if r_node.right else None
    #
    #         l_queue.append(l_node.right) if l_node.right else None
    #         r_queue.append(r_node.left) if r_node.left else None
    #
    #     return True if len(l_queue) == 0 and len(r_queue) == 0 else False


if __name__ == '__main__':
    tc1 = TreeNode(1)
    tc2 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))
    tc3 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    tc4 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    print(Solution().isSymmetric(root=tc1))
