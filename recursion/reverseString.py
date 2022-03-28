from typing import List, Optional


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.my_recursion(s, 0)

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     answer, tail = self.my_recursive(head)
    #     return answer.next
    #
    # def my_recursive(self, head: Optional[ListNode]):
    #     if head is None:
    #         head = tail = ListNode(0)
    #         return head, tail
    #
    #     cur = head
    #     new_head, tail = self.my_recursive(head.next)
    #     tail.next = cur
    #     tail = tail.next
    #     tail.next = None
    #     return new_head, tail

    @staticmethod
    def tail_recursion(my_string: str):
        def helper(ls, acc):
            if len(ls) == 0:
                return acc
            return helper(ls[1:], ls[0] + acc)

        return helper(my_string, "")


if __name__ == '__main__':
    # my_list = ['J', 'U', 'L', 'I', 'E']
    # testcase = ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ", "a", " ", "c", "a", "n", "a",
    #             "l", ":", " ", "P", "a", "n", "a", "m", "a"]
    # solution = Solution()
    # solution.reverseString(testcase)
    # print(my_list)

    print(Solution.tail_recursion('julieyang'))
