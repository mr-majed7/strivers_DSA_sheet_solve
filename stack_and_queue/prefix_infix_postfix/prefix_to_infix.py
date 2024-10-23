#https://www.geeksforgeeks.org/problems/prefix-to-infix-conversion/1
class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        stack = []
        
        for i in range(len(pre_exp)-1,-1,-1):
            if prefix[i].isalnum():
                stack.append(prefix[i])
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                stack.append(f"({top1}{prefix[i]}{top2})")
        return stack[-1]
