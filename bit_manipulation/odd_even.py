# https://www.geeksforgeeks.org/problems/odd-or-even3618/1


class Solution:
    def oddEven(ob, N):
        # code here
        if (N ^ 1) == N - 1:
            # If a Number is ODD XOR of tham number will be n-1
            return "odd"

        return "even"
