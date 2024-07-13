# https://www.geeksforgeeks.org/problems/implement-stack-using-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implement-stack-using-linked-list


class MyStack:
    # class StackNode:

    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None

    # Function to push an integer into the stack.
    def __init__(self):
        self.top = None

    def push(self, data):
        temp = StackNode(data)

        if self.top == None:
            self.top = temp
        else:
            temp.next = self.top
            self.top = temp

        # Add code here

    # Function to remove an item from top of the stack.
    def pop(self):
        if self.top == None:
            return -1
        x = self.top.data
        self.top = self.top.next
        return x

        # Add code here
