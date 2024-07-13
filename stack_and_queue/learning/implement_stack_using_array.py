# https://www.geeksforgeeks.org/problems/implement-stack-using-array/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implement-stack-using-array


class MyStack:
    def __init__(self):
        self.arr = []
        self.top = -1

    # Function to push an integer into the stack.
    def push(self, data):
        # add code here
        self.top += 1
        self.arr.append(data)

    # Function to remove an item from top of the stack.
    def pop(self):
        # add code here
        if len(self.arr) == 0:
            return -1
        val = self.arr.pop(self.top)
        self.top -= 1
        return val
