from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        def make_list(root: Optional[Node]) -> Optional[Node]:
            head_node, cur_node = root, root
            prev_node, next_node = None, None
            while cur_node:
                if cur_node.child:
                    head_child_nodes, tail_child_nodes = make_list(cur_node.child)
                    next_node = cur_node.next
                    # has only one child
                    if head_child_nodes == tail_child_nodes:
                        tail_child_nodes.prev = cur_node
                        cur_node.next = tail_child_nodes

                        tail_child_nodes.next = next_node
                        if next_node:
                            next_node.prev = tail_child_nodes
                    else:
                        tail_child_nodes.next = next_node
                        if next_node:
                            next_node.prev = tail_child_nodes

                        cur_node.next = head_child_nodes
                        head_child_nodes.prev = cur_node

                    cur_node.child = None
                    prev_node = tail_child_nodes
                    cur_node = next_node
                else:
                    prev_node = cur_node
                    cur_node = cur_node.next
            return head_node, prev_node
        answer, _ = make_list(head)
        return answer


def print_node(head: Node):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
    print('=========')


def get_12453():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)

    node_1.next = node_2
    node_2.prev = node_1
    node_2.next = node_3
    node_2.child = node_4

    node_3.prev = node_2

    node_4.next = node_5

    node_5.prev = node_4

    return node_1


def get_12345():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)

    node_1.child = node_2
    node_2.child = node_3
    node_3.child = node_4
    node_4.child = node_5

    return node_1


if __name__ == '__main__':
    tc0 = get_12453()
    tc1 = get_12345()

    s = Solution()
    ans = s.flatten(head=tc1)
    print_node(ans)
