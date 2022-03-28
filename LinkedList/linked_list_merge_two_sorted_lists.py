# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = list()
        cur = list1
        while cur:
            merged_list.append(cur)
            cur = cur.next

        cur = list2
        while cur:
            merged_list.append(cur)
            cur = cur.next

        merged_list.sort(key=lambda x: x.val)

        if len(merged_list) == 0:
            return None

        merged_list_head = merged_list.pop(0)
        cur = merged_list_head
        for node in merged_list:
            cur.next = node
            cur = cur.next

        return merged_list_head

    def merge_two_lists_optimized(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 or list2
        return head.next


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

s = Solution()
s.mergeTwoLists(list1, list2)
# print(s.merge_two_lists_optimized(list1, list2))
