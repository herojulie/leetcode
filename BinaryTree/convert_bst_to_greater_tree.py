from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    total_sum = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node: Optional[TreeNode]):
            if node is None:
                return
            helper(node.right)
            node.val += Solution.total_sum
            Solution.total_sum = node.val
            helper(node.left)

        helper(root)
        return root


def print_tree(root: TreeNode):
    if root is None:
        return
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)


if __name__ == '__main__':
    tc1 = TreeNode(4,   # root
                   TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))),    # left
                   TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))    # right
    s = Solution()
    print_tree(s.convertBST(root=tc1))
