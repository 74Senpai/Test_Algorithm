class Solution:
  # PASS: 3ms, 18.02MB
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_row, dict_col= {}, {}
        three_grid = { 1 : {0}, 2 : {0}, 3 : {0}}
        for row in range(9):
            count = -1
            if row == 3 or row == 6:
                three_grid = { 1 : {0}, 2 : {0}, 3 : {0}}

            for col in range(9):
                curr = board[row][col]
                count += 1
                if curr == ".":
                    continue
                if curr not in dict_col:
                    dict_col[curr] = {col}
                else:
                    if col in dict_col[curr]:
                        return False
                    dict_col[curr].add(col)
                
                if curr not in dict_row:
                    dict_row[curr] = {row}
                else:
                    if row in dict_row[curr] :
                        return False
                    dict_row[curr].add(row)

                if count >= 6 :
                    key = 3
                elif count >= 3:
                    key = 2
                else:
                    key = 1
                
                if curr in three_grid[key]:
                    print(three_grid)
                    return False
                three_grid[key].add(curr)

        return True                        
