# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev: ListNode = None

        while head:
            next_ = head.next
            head.next = prev
            prev = head
            head = next_

        return prev

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev


def print_node(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    tc1 = ListNode(1, ListNode(2, ListNode(3)))

    s = Solution()
    ans = s.reverseList2(head=tc1)
    print_node(ans)
