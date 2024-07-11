# https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bit-manipulation
class Solution:
    def bitManipulation(self, num, i):
        # Code here
        geti = (num & (1 << (i - 1))) >> (i - 1)
        seti = num | (1 << i - 1)
        cleari = num & (~(1 << i - 1))

        print(f" {geti} {seti} {cleari}")
