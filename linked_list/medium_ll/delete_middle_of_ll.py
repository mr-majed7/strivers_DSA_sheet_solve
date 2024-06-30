# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        slow = head
        fast = head
        slow_prev = None

        while fast is not None and fast.next is not None:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        slow_prev.next = slow.next
        slow.next = None
        return head
