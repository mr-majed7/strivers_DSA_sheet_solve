# https://www.geeksforgeeks.org/problems/postfix-to-prefix-conversion/1


class Solution:
    def postToPre(self, post_exp):
        # Code here
        stack = []
        
        for c in post_exp:
            if c.isalnum():
                stack.append(c)
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                stack.append(f"{c}{top2}{top1}")
        return stack.pop()
