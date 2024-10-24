# https://www.geeksforgeeks.org/problems/prefix-to-postfix-conversion/1

class Solution:
    def preToPost(self, pre_exp):
        # Code here
        stack = []
        
        for i in range(len(pre_exp)-1,-1,-1):
            if pre_exp[i].isalnum():
                stack.append(pre_exp[i])
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                stack.append(f"{top1}{top2}{pre_exp[i]}")
        return stack.pop()
