# https://leetcode.com/problems/set-matrix-zeroes/description/


# A BIT FASTER
class Solution:
    """
    To solve this problem, we need to keep track of the rows and columns that are to be set to zero.
    We can do this by creating two lists, one for the rows and one for the columns.
    We can then iterate through the matrix and add the row and column to the respective lists.
    Once we have the rows and columns, we can iterate through the lists and set the rows and columns to zero.
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_n = len(matrix)
        column_n = len(matrix[0])

        rows = []
        columns = []

        for r in range(rows_n):
            for c in range(column_n):
                if (
                    matrix[r][c] == 0
                ):  # if the element is 0, add the row and column to their respective lists
                    rows.append(r)
                    columns.append(c)

        for r in rows:  # set the rows and columns to zero
            for c in range(column_n):
                matrix[r][c] = 0

        for c in columns:  # set the rows and columns to zero
            for r in range(rows_n):
                matrix[r][c] = 0


# O(1) SPACE SOLUTION
class Solution:
    """
    We will use the first row and first column to keep track of the rows and columns that are to be set to zero.
    We take extra variable col0 to solve the issue with taking cell [0][0] twice.
    We will iterate through the matrix and set the first element of the row and column to zero if the element is zero.
    We will then iterate through the matrix and set the element to zero if the first element of the row or column is zero.
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1  # to solve the issue with taking cell [0][0] twice

        rows = len(matrix)
        columns = len(matrix[0])

        for r in range(
            rows
        ):  # iterate through the matrix and set the first element of the row and column to zero if the element is zero
            for c in range(columns):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0

                    if c != 0:
                        matrix[0][c] = 0
                    else:
                        col0 = 0

        for r in range(
            1, rows
        ):  # iterate through the matrix and set the element to zero if the first element of the row or column is zero
            for c in range(1, columns):
                if matrix[r][c] != 0:
                    if matrix[r][0] == 0 or matrix[0][c] == 0:
                        matrix[r][c] = 0
        if matrix[0][0] == 0:  # set the first row to zero
            for c in range(columns):
                matrix[0][c] = 0

        if col0 == 0:  # set the first column to zero
            for r in range(rows):
                matrix[r][0] = 0
