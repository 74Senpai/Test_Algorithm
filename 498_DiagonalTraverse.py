class Ver1:
  # FAILD: logic base
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row,col = 0,0
        isUp = False
        res = []
        while True:
            if row == col == len(mat) - 1:
                break
            if row == 0:
                isUp = False
                col += 1
            elif col == 0:
                isUp = True
                row += 1

            if isUp:
                row -= 1
                col += 1
            else:
                row += 1
                col -= 1
            
        return res
                
                
