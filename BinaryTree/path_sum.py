from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node: TreeNode, cur_sum):
            if node.left is None and node.right is None:
                return True if cur_sum + node.val == targetSum else False
            left = helper(node.left, cur_sum + node.val) if node.left else False
            right = helper(node.right, cur_sum + node.val) if node.right else False
            return left or right
        if root is None:
            return False
        return helper(root, 0)

    def hasPathSum_better(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        return self.hasPathSum_better(root.left, targetSum - root.val) or self.hasPathSum_better(root.right, targetSum - root.val)


if __name__ == '__main__':
    tc1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tc2 = TreeNode(11, TreeNode(7), TreeNode(2))
    tc3 = TreeNode(1, TreeNode(2))
    print(Solution().hasPathSum_better(root=tc3, targetSum=2))
