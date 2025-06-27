def generate(self, numRows: int) -> list[list[int]]:
    triangle = [[1] * numRows for i in range(numRows)]
    for x in range(1, numRows):
        for y in range(1 , x):
            triangle[x][y] = triangle[x - 1][y - 1] + triangle[x - 1][y]

    return triangle
print(generate(None, 5))