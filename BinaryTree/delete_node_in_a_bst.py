from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            left_most = root.right
            while left_most.left:
                left_most = left_most.left
            root.val = left_most.val
            root.right = self.deleteNode(root.right, root.val)
        return root


def inorder_traverse(root: TreeNode) -> None:
    if root is None:
        return
    inorder_traverse(root.left)
    print(root.val)
    inorder_traverse(root.right)


if __name__ == '__main__':
    tc1 = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    s = Solution()
    ans = s.deleteNode(root=tc1, key=3)
    inorder_traverse(ans)
