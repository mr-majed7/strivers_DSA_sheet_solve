# https://leetcode.com/problems/rotate-image/


class Solution:
    """
    If we notice carefully, we can see that this problem can be solved by first Transpose the matrix and then reverse each row.
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(len(matrix)):  # Transpose The Matrix
            for c in range(r):
                matrix[r][c], matrix[c][r] = (
                    matrix[c][r],
                    matrix[r][c],
                )  # Transpose The Matrix

        for r in matrix:  # Reverse Each Row
            r.reverse()
