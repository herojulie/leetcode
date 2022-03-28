"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.org_node_id_to_new_node_map = {None: None}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head in self.org_node_id_to_new_node_map:
            return self.org_node_id_to_new_node_map[head]

        new_node = Node(head.val)
        self.org_node_id_to_new_node_map[head] = new_node
        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)
        return new_node


def print_node(head: Node):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
    print('=========')


if __name__ == '__main__':
    node_1 = Node(7)
    node_2 = Node(13)
    node_3 = Node(11)
    node_4 = Node(10)
    node_5 = Node(1)

    node_1.next = node_2
    node_1.random = None

    node_2.next = node_3
    node_2.random = node_1

    node_3.next = node_4
    node_3.random = node_5

    node_4.next = node_5
    node_4.random = node_3

    node_5.next = None
    node_5.random = node_1

    s = Solution()
    ans = s.copyRandomList(head=node_5)
    print_node(ans)

