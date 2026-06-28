class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rule1:rows
        for n in board:
            row = set()
            for a in n:
                if a==".":
                    continue
                if a in row:
                    return False
                row.add(a)

        #rule2:columns
        for col in range(9):
            column = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in column:
                    return False
                column.add(board[row][col])

        #rule3: 3x3
        
        for box_col in range(0,9,3):
            for box_row in range(0,9,3):
                box = set()
                for r in range(3):
                    for c in range(3):
                        if board[box_row +r][box_col+c] ==".":
                            continue
                        if board[box_row + r][box_col+c] in box:
                            return False
                        box.add(board[box_row+r][box_col+c])
        return True


