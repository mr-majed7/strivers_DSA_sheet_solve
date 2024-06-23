# https://leetcode.com/problems/reverse-linked-list/description/


# ITERATIVE SOLUTION
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        last = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev


# RECURSIVE SOLUTION


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
