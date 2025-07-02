class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1] * (rowIndex + 1) 
        if rowIndex <= 1:
            return row
            
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]

        return row