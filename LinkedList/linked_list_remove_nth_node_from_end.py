# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        cur: ListNode = head
        length: int = 1

        while cur.next is not None:
            cur = cur.next
            length += 1

        # length - n = index of Nth node
        cur = head
        for i in range(1, length - n):
            cur = cur.next
        cur.next = cur.next.next

        return head
