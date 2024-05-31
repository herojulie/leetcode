from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     if not head or not head.next or not head.next.next:
    #         return False
    #     turtle, rabbit = head.next, head.next.next
    #     while turtle != rabbit:
    #         if not rabbit.next or not rabbit.next.next:
    #             return False
    #         turtle = turtle.next
    #         rabbit = rabbit.next.next
    #
    #     return True
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        turtle, rabbit = head, head
        while rabbit.next and rabbit.next.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if turtle == rabbit:
                return True
        return False


if __name__ == '__main__':
    # tc1
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(3)
    node_5 = ListNode(3)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_3

    s = Solution()
    print(s.hasCycle(head=node_1))

