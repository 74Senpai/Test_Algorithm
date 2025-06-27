def generate(self, numRows: int) -> list[list[int]]:
    triangle = [[1] * numRows for i in range(numRows)]
    triangle[0] = triangle[0][0:1]
    for x in range(1, numRows):
        for y in range(1 , x):
            triangle[x][y] = triangle[x - 1][y - 1] + triangle[x - 1][y]
        triangle[x] = triangle[x][0:x + 1]
      
    return triangle
print(generate(None, 5))