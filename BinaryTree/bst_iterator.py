from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.queue = deque([])
        self._traverse(root)

    def _traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        self._traverse(root.left)
        self.queue.append(root.val)
        self._traverse(root.right)

    def next(self) -> int:
        print(self.queue[0])
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue)


if __name__ == '__main__':
    tc1 = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))

    # Your BSTIterator object will be instantiated and called as such:
    bSTIterator = BSTIterator(root=tc1)
    bSTIterator.next()  # return 3
    bSTIterator.next()  # return 7
    bSTIterator.hasNext()  # return True
    bSTIterator.next()  # return 9
    bSTIterator.hasNext()  # return True
    bSTIterator.next()  # return 15
    bSTIterator.hasNext()  # return True
    bSTIterator.next()  # return 20
    bSTIterator.hasNext()  # return False
