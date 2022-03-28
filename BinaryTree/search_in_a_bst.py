from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


def print_treenode(root: Optional[TreeNode]):
    if root is None:
        return
    print_treenode(root.left)
    print(root.val)
    print_treenode(root.right)


if __name__ == '__main__':
    tc1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    s = Solution()
    res = s.searchBST(root=tc1, val=4)
    print('root:', res.val)
    print_treenode(res)
