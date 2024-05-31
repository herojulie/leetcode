from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        answer: List[List[int]] = []
        queue = deque([root])

        while queue:
            size = len(queue)
            level_node = []
            while size > 0:
                node = queue.popleft()
                level_node.append(node.val)
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
                size -= 1
            answer.append(level_node)

        return answer

    # from cheetsheet book on Sep 6 2023
    def levelOrderSerialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return None
        
        nb = []
        q = [root]
        while q:
            cur = q.pop(0)
            if cur is None:
                nb.append("#")
                continue
            nb.append(str(cur.val))
            q.extend([cur.left, cur.right])
        
        return ",".join(nb)
    
    def levelOrderDeserialize(self, nb: list[str]):
        if len(nb) == 0:
            return None
        
        root = TreeNode(nb[0])
        q = [root]

        for i in range(1, len(nb) - 1, 2):
            parent = q.pop(0)
            left = nb[i]
            if left == "#":
                parent.left = None
            else:
                parent.left = TreeNode(left)
                q.append(parent.left)
            
            right = nb[i + 1]
            if right == "#":
                parent.right = None
            else:
                parent.right = TreeNode(right)
                q.append(parent.right)
        
        return root


if __name__ == '__main__':
    tc1 = TreeNode(3, TreeNode(9), TreeNode(2, TreeNode(5), TreeNode(7)))
    tc2 = TreeNode(1)
    tc3 = []

    s = Solution()
    print(s.levelOrder(root=tc1))
    sr = s.levelOrderSerialize(tc1)
    dsr = s.levelOrderDeserialize([c for c in sr if c != ','])
    print(dsr)
