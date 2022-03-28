# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode], depth: int) -> int:
            if root is None:
                return depth

            left_depth = helper(root.left, depth + 1)
            right_depth = helper(root.right, depth + 1)
            return left_depth if left_depth > right_depth else right_depth

        return helper(root, 0)
