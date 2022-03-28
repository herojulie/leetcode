from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        def preorder_traversal(parent: TreeNode, ans: [int]) -> [int]:
            if parent is None:
                return ans
            ans.append(parent.val)
            ans = preorder_traversal(parent.left, ans)
            ans = preorder_traversal(parent.right, ans)
            return ans
        return preorder_traversal(root, [])

    # iterate
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        cur = root
        stack = deque()

        while stack or cur:
            while cur:
                ans.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                cur = cur.left

            if stack:
                cur = stack.pop()

        return ans


if __name__ == '__main__':
    tc1 = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    tc2 = None
    tc3 = TreeNode(1)

    tc4 = TreeNode(10)
    tc4.left = TreeNode(20)
    tc4.right = TreeNode(30)
    tc4.left.left = TreeNode(40)
    tc4.left.left.left = TreeNode(70)
    tc4.left.right = TreeNode(50)
    tc4.right.left = TreeNode(60)
    tc4.left.left.right = TreeNode(80)

    s = Solution()
    print(s.preorderTraversal(root=tc4))
