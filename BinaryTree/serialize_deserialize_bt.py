# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def helper(node: TreeNode):
            if node:
                result.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                result.append('#')
        result = []
        helper(root)
        return ' '.join(result)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper():
            val = next(data_it)
            if val == '#':
                return None
            node = TreeNode(val)
            node.left = helper()
            node.right = helper()
            return node
        data_it = iter(data.split())
        return helper()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
if __name__ == '__main__':
    tc1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    serialized = Codec().serialize(root=tc1)
    de_serialized = Codec().deserialize(serialized)
    print(serialized)

    # ser = Codec()
    # deser = Codec()
    # ans = deser.deserialize(ser.serialize(root))
