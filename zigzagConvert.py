def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    row = 0
    moveRow = 1 
    zigzag_array = [[''] * len(s) for _ in range(numRows)]
    cell = 0
    moveCell = 0
    for i in range(len(s)):
        if row == 0:
            moveRow = 1
            moveCell = 0
        elif row == numRows - 1:
            moveRow = -1
            moveCell = 1
        zigzag_array[row][cell] = s[i]
        cell += moveCell
        row = row + moveRow

    s_convert = ""
    for row in zigzag_array:
        for i in row[:cell + 1]:
            s_convert += i
                
    return s_convert


print(convert(None, "PAYPALISHIRING", 3))