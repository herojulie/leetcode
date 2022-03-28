from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def postorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        def postorder_traversal(node: TreeNode, answer: [int]) -> [int]:
            if node is None:
                return answer
            answer = postorder_traversal(node.left, answer)
            answer = postorder_traversal(node.right, answer)
            answer.append(node.val)
            return answer

        return postorder_traversal(root, [])

    # iterative
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pass


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
    print(s.postorderTraversal(root=tc4))
