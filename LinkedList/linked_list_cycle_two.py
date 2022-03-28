# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_length(self, head: ListNode) -> int:
        length: int = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next
        return length

    def set_start_node(self, headA: ListNode, headB: ListNode) -> tuple[ListNode, ListNode]:
        lenA = self.get_length(headA)
        lenB = self.get_length(headB)

        if lenA == lenB:
            return headA, headB
        if lenA > lenB:
            move_count = lenA - lenB
            cur: ListNode = headA
            while move_count > 0:
                cur = cur.next
                move_count -= 1
            return cur, headB
        if lenA < lenB:
            move_count = lenB - lenA
            cur: ListNode = headB
            while move_count > 0:
                cur = cur.next
                move_count -= 1
            return headA, cur

    def method1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        startA, startB = self.set_start_node(headA, headB)

        curA: ListNode = startA
        curB: ListNode = startB

        while curA is not None and curB is not None:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next

        return None

    def get_last_node_and_length(self, head: ListNode) -> tuple[Optional[ListNode], int]:
        cur: ListNode = head
        length: int = 1
        while cur.next is not None:
            cur = cur.next
            length += 1
        return cur, length

    def method2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # find the last node of list A
        last_node_a, length_a = self.get_last_node_and_length(headA)

        # make listA a circular list
        last_node_a.next = headA

        cur_b: ListNode = headB
        while length_a > 0:
            cur_b = cur_b.next
            length_a -= 1

        new_head = headB
        while new_head is not None and cur_b is not None:
            if new_head == cur_b:
                return cur_b
            new_head = new_head.next
            cur_b = cur_b.next

        last_node_a.next = None

        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        return self.method2(headA, headB)


if __name__ == '__main__':
    head_a = ListNode(4)
    head_a.next = ListNode(1)
    head_a.next.next = ListNode(8)
    head_a.next.next.next = ListNode(4)
    head_a.next.next.next.next = ListNode(5)

    head_b = ListNode(5)
    head_b.next = ListNode(6)
    head_b.next.next = head_a.next

    s: Solution = Solution()
    ixn_node = s.getIntersectionNode(head_a, head_b)
    print(ixn_node.val)




