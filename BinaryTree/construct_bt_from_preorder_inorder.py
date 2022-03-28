from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for i, val in enumerate(inorder):
            indices[val] = i

        def helper(low, high) -> TreeNode:
            if low > high:
                return None
            parent = TreeNode(preorder.pop(0))
            mid = indices[parent.val]
            parent.left = helper(low, mid - 1)
            parent.right = helper(mid + 1, high)
            return parent

        return helper(0, len(inorder) - 1)


if __name__ == '__main__':
    ans = Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
    print(ans)
