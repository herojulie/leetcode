from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for i, val in enumerate(inorder):
            indices[val] = i

        def helper(start: int, end: int) -> TreeNode:
            if start > end:
                return None
            parent = TreeNode(postorder.pop())
            parent.right = helper(indices[parent.val] + 1, end)
            parent.left = helper(start, indices[parent.val] - 1)
            return parent
        return helper(0, len(inorder) - 1)


if __name__ == '__main__':
    ans = Solution().buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
    print(ans)
