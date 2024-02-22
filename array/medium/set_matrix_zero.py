#https://leetcode.com/problems/set-matrix-zeroes/description/

#A BIT FASTER
class Solution:
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
                if matrix[r][c] == 0:
                    rows.append(r)
                    columns.append(c)
        

        for r in rows:
            for c in range(column_n):
                matrix[r][c] = 0

     
        for c in columns:
            for r in range(rows_n):
                matrix[r][c] = 0


#O(1) SPACE SOLUTION
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1

        rows = len(matrix)
        columns = len(matrix[0])

        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    
                    if c !=0:
                        matrix[0][c] = 0
                    else:
                        col0 = 0
                    
        for r in range(1,rows):
                for c in range(1,columns):
                    if matrix[r][c] !=0:
                        if matrix[r][0] == 0 or matrix[0][c] == 0:
                            matrix[r][c] = 0
        if matrix[0][0] == 0:
            for c in range(columns):
                matrix[0][c] = 0

        if col0 == 0:
            for r in range(rows):
                matrix[r][0] = 0