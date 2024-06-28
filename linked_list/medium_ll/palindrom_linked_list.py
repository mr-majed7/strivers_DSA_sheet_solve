# https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev = None
            current = head
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev

        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        new_head = reverse(slow.next)

        first = head
        second = new_head

        while second is not None:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        reverse(new_head)

        return True
