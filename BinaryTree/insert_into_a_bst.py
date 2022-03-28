from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        def helper(head: Optional[TreeNode]):
            if head is None:
                return None

            if head.val > val and head.left is None:
                head.left = TreeNode(val)
                return
            elif head.val < val and head.right is None:
                head.right = TreeNode(val)
                return
            elif head.val > val:
                helper(head.left)
            elif head.val < val:
                helper(head.right)
            else:
                return
        helper(root)
        return root

    def insertIntoBST_copied(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST_copied(root.left, val)
        else:
            root.right = self.insertIntoBST_copied(root.right, val)
        return root


def print_tree_node(root: Optional[TreeNode]):
    if root is None:
        return
    print_tree_node(root.left)
    print(root.val)
    print_tree_node(root.right)


if __name__ == '__main__':
    tc1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    tc2 = TreeNode(40, TreeNode(20, TreeNode(10), TreeNode(30)), TreeNode(60, TreeNode(50), TreeNode(70)))
    s = Solution()
    ans = s.insertIntoBST(root=tc2, val=25)
    print_tree_node(ans)
