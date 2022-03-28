import os
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node: TreeNode, depth: int) -> int:
            if node is None:
                return depth - 1

            left_depth = helper(node.left, depth + 1)
            right_depth = helper(node.right, depth + 1)
            return max(left_depth, right_depth)
        return helper(root, 1)


if __name__ == '__main__':
    tc1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    tc2 = TreeNode(1)
    tc3 = []

    print(Solution().maxDepth(root=None))
