#https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(1,numRows+1):
            current = 1
            currentRow = [1]
            for j in range(1,i):
                current *=(i-j)
                current //= j
                currentRow.append(current)
            triangle.append(currentRow)    
        return triangle
