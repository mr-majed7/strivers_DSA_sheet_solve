#https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c] #Transpose The Matrix

        for r in matrix:
            r.reverse() #Reverse The Rows