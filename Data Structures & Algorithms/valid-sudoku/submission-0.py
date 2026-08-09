class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen_row = set()

            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen_row:
                    return False
                seen_row.add(board[r][c])
        
        for c in range(9):
            seen_col = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen_col:
                    return False
                seen_col.add(board[r][c])
        #the 3x3 squares
        for box_row in range(0, 9, 3):   #starr at zero, stop before 9 and move 3 spaces each time
            for box_col in range(0, 9, 3):
                seen = set()
                for r in range(box_row, box_row+3):
                    for c in range(box_col, box_col+3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in seen:
                            return False
                        seen.add(board[r][c])
        return True



        