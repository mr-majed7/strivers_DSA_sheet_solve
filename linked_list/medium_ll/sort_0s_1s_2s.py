# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=given-a-linked-list-of-0s-1s-and-2s-sort-it

# User function Template for python3
"""
Your task is to segregate the list of
0s,1s and 2s.

Function Arguments: head of the original list.
Return Type: head of the new list formed.

{
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
}

"""


class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        # code here
        if head is None or head.next is None:
            return head

        zero_head = Node(-1)
        one_head = Node(-1)
        two_head = Node(-1)

        zero = zero_head
        one = one_head
        two = two_head
        current = head

        while current != None:
            if current.data == 0:
                zero.next = current
                zero = zero.next

            elif current.data == 1:
                one.next = current
                one = one.next

            else:
                two.next = current
                two = two.next

            current = current.next

        zero.next = one_head.next if one_head.next != None else two_head.next
        one.next = two_head.next
        two.next = None

        return zero_head.next
