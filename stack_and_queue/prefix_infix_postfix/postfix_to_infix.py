# https://www.geeksforgeeks.org/problems/postfix-to-infix-conversion/1

class Solution:
    def postToInfix(self, postfix):
        # Code here
        stack = []
        for c in postfix:
            if c.isalnum():
                stack.append(c)
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                stack.append(f'({top2}{c}{top1})')
        return stack.pop()
