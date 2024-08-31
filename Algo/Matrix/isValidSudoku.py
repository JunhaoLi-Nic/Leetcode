
def isValidSudoku(board) -> bool:
    rows = [set() for x in range(9)]
    columns = [set() for x in range(9)]
    squares = [[set() for x in range(3)] for y in range(3)]

    for x in range(9):
        for y in range(9):
            cell_value = board[x][y]
            if cell_value == ".":
                continue
            if cell_value in rows[x] or cell_value in columns[y] or cell_value in squares[x // 3][y // 3]:
                return False

            rows[x].add(cell_value)
            columns[y].add(cell_value)
            squares[x // 3][y // 3].add(cell_value)

    return True


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))