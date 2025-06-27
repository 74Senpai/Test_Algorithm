def generate(self, numRows: int) -> list[list[int]]:
    triangle = [[1] * numRows for i in range(numRows)]
    row = [[]] * numRows
    row[0] = [1]
    row[1] = [1,1]
    for x in range(1, numRows):
        for y in range(1 , numRows - x):
            triangle[x][y] = triangle[x][y - 1] + triangle[x - 1][y]
            row[x].append(triangle[x][y])

    return row

print(generate(None, 5))