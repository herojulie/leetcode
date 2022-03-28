# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional, List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.subtrees = defaultdict(list)

    def postorder_traverse(self, root_node: Optional[TreeNode]) -> str:
        if root_node is None:
            return None
        left = self.postorder_traverse(root_node.left)
        right = self.postorder_traverse(root_node.right)
        node_id = f'{left}, {right}, {str(root_node.val)}'
        self.subtrees[node_id].append(root_node)
        return node_id

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.postorder_traverse(root)
        return [self.subtrees[node_id][0] for node_id in self.subtrees if len(self.subtrees[node_id]) > 1]


# [1,2,3,4,null,2,4,null,null,4]
if __name__ == '__main__':
    n4a, n4b, n4c = TreeNode(4), TreeNode(4), TreeNode(4)
    n2a = TreeNode(2, n4a)
    n2b = TreeNode(2, n4b)
    n3a = TreeNode(3, n2b, n4c)
    n1a = TreeNode(1, n2a, n3a)

    print(Solution().findDuplicateSubtrees(n1a))
