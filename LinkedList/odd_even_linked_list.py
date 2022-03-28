from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        ans = ListNode(0)
        ans_tail = ans

        dummy_head = ListNode(0, head)
        prev = dummy_head
        cur = head
        count = 1
        while cur:
            if count % 2 == 1:
                prev.next = cur.next
                ans_tail.next = cur
                ans_tail = ans_tail.next
                cur.next = None
            else:
                prev = prev.next
            cur = prev.next
            count += 1

        ans_tail.next = dummy_head.next if dummy_head.next else None
        return ans.next if ans.next else None


def print_node(head: ListNode):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
    print('=========')


if __name__ == '__main__':
    head_node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = Solution()
    t1 = s.oddEvenList(head=head_node)
    print_node(t1)

    t2 = s.oddEvenList(head=ListNode(0))
    print_node(t2)
