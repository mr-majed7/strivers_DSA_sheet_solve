# https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1


class Solution:
    def get(self, a, b):
        # code here
        b = a + b
        a = b - a
        b = b - a
        return a, b
