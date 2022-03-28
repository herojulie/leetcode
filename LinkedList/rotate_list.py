from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        cur = head
        org_tail = head
        length = 0
        while cur:
            org_tail = cur
            cur = cur.next
            length += 1

        if k % length== 0:
            return head

        cur = head
        count = 1
        while count < length - (k % length):
            cur = cur.next
            count += 1

        new_head = cur.next
        org_tail.next = head
        cur.next = None

        return new_head


def print_node(head: ListNode):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
    print('==============')


if __name__ == '__main__':
    tc1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    s = Solution()
    ans = s.rotateRight(head=tc1, k=1)
    print_node(ans)
