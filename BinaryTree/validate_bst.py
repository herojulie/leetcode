from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(head: Optional[TreeNode], left, right) -> bool:
            if head is None:
                return True

            if not left < head.val < right:
                return False
            return helper(head.left, left, head.val) and helper(head.right, head.val, right)
        return helper(root, float('-inf'), float('inf'))


class SolutionCopied:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.BST(root, float("-inf"), float("inf"))

    def BST(self, root, left, right):

        if root == None:
            return True

        if not left < root.val < right:
            return False

        return self.BST(root.left, left, root.val) and self.BST(root.right, root.val, right)


if __name__ == '__main__':
    tc1 = TreeNode(2, TreeNode(1), TreeNode(3))
    tc2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(Solution().isValidBST(root=tc1))
