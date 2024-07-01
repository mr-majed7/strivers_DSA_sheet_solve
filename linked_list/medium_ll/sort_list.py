# https://leetcode.com/problems/sort-list/


# MERGE SORT
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMiddle(head):
            if head is None:
                return head

            slow = head
            fast = head

            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next

            return head

        def merge(left, right):
            dummy = ListNode(0)
            current = dummy

            while left is not None and right is not None:
                if left.val <= right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next

            if left is not None:
                current.next = left
            else:
                current.next = right

            return dummy.next

        def mergeSort(head):
            if head is None or head.next is None:
                return head

            middle = getMiddle(head)
            middle_next = middle.next

            middle.next = None

            left = mergeSort(head)
            right = mergeSort(middle_next)

            return merge(left, right)

        return mergeSort(head)


# LEETCODE ACCEPTED
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        temp = head
        sorted_list = []

        while temp:
            sorted_list.append(temp.val)
            temp = temp.next

        sorted_list.sort()

        temp = head

        for val in sorted_list:
            temp.val = val
            temp = temp.next

        return head
