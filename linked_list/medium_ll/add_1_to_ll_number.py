# https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=add-1-to-a-number-represented-as-linked-list

# User function Template for python3

"""

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
"""


class Solution:
    def addOne(self, head):
        # Returns new head of linked List.

        def helper(current):
            if current == None:
                return 1

            carry = helper(current.next)
            current.data += carry

            if current.data < 10:
                return 0

            current.data = 0
            return 1

        carry = helper(head)

        if carry != 0:
            new_node = Node(1)
            new_node.next = head
            head = new_node

        return head
