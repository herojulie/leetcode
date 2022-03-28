# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList_iterate(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = head
        while head.next != None:
            temp = head.next
            head.next = head.next.next

            if new_head is not None:
                temp.next = new_head
            new_head = temp

        return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer, tail = self.my_recursive(head)
        return answer.next

    def my_recursive(self, head: Optional[ListNode]):
        if head is None:
            head = tail = ListNode(0)
            return head, tail

        cur = head
        new_head, tail = self.my_recursive(head.next)
        tail.next = cur
        tail = tail.next
        tail.next = None
        return new_head, tail

    def print_list_node(self, head: ListNode):
        if head is None:
            return
        print(head.val)
        self.print_list_node(head.next)


if __name__ == '__main__':
    testcase = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    s = Solution()
    result = s.reverseList(testcase)
    s.print_list_node(result)
