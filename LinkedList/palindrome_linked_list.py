from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return True

        turtle = head
        rabbit = head
        queue = []
        while rabbit and rabbit.next:
            queue.append(turtle.val)
            turtle = turtle.next
            rabbit = rabbit.next.next

        turtle = turtle.next if rabbit else turtle

        while turtle:
            n = queue.pop()
            if turtle.val != n:
                return False
            turtle = turtle.next

        return True if len(queue) == 0 else False


if __name__ == '__main__':
    s = Solution()
    tc1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    tc2 = ListNode(0, ListNode(0))
    tc3 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1))))))
    tc4 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    print(s.isPalindrome(head=tc1))
    print(s.isPalindrome(head=tc2))
    print(s.isPalindrome(head=tc3))
    print(s.isPalindrome(head=tc4))
