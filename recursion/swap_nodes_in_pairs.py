# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        swapped = self.swapPairs(head.next.next)

        new_head = head.next
        head, new_head = new_head, head
        head.next = swapped
        new_head.next = head
        return new_head


if __name__ == '__main__':
    testcase = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    solution = Solution()
    solution.swapPairs(testcase)
    print(testcase)
