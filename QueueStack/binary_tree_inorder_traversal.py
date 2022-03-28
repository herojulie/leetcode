# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode], ans: List[int]):
            if not node:
                return ans
            if node.left:
                ans = dfs(node.left, ans)
            ans.append(node.val)
            if node.right:
                ans = dfs(node.right, ans)
            return ans

        if not root:
            return root
        return dfs(root, [])


if __name__ == '__main__':
    n3 = TreeNode(3)
    n2 = TreeNode(2, left=n3)
    n1 = TreeNode(1, right=n2)
    print(Solution().inorderTraversal(None))
