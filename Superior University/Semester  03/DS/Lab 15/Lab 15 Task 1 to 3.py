# Task 1: Solving the N-Queens Problem Using Backtracking 
# Objective: Understand backtracking by solving the N-Queens problem, where N queens 
# must be placed on an N × N chessboard so that no two queens attack each other. 



def solve_n_queens(n):
    def backtrack(row, cols, pos_diags, neg_diags, board, solutions):
        if row == n:
            solutions.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row + col) in pos_diags or (row - col) in neg_diags:
                continue 
            board[row][col] = 'Q'
            cols.add(col)
            pos_diags.add(row + col)
            neg_diags.add(row - col)
            backtrack(row + 1, cols, pos_diags, neg_diags, board, solutions)
            board[row][col] = '.'
            cols.remove(col)
            pos_diags.remove(row + col)
            neg_diags.remove(row - col)

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0, set(), set(), set(), board, solutions)
    return solutions
for solution in solve_n_queens(4):
    for row in solution:
        print(row)
    print()

# Task 2: Generating All Possible Permutations of a String 
# Objective: Learn backtracking with recursion by generating all possible permutations of a 
# given string. 


def permute(s):
    def backtrack(start):
        if start == len(chars):
            result.append("".join(chars))
            return
        seen = set()
        for i in range(start, len(chars)):
            if chars[i] in seen:
                continue 
            seen.add(chars[i])
            chars[start], chars[i] = chars[i], chars[start] 
            backtrack(start + 1)
            chars[start], chars[i] = chars[i], chars[start]

    chars = list(s)
    result = []
    backtrack(0)
    return result
print(permute("ABC"))


# Task 3: Solving the Sudoku Puzzle Using Backtracking 
# Objective: Apply backtracking to solve a Sudoku puzzle, where a 9×9 grid must be filled 
# following Sudoku rules. 

def solve_sudoku(board):
    def is_valid(row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def find_empty():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def backtrack():
        empty = find_empty()
        if not empty:
            return True 

        row, col = empty
        for num in range(1, 10):
            if is_valid(row, col, num):
                board[row][col] = num
                if backtrack():
                    return True
                board[row][col] = 0 
        return False
    backtrack()
    return board
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0], 
    [6, 0, 0, 1, 9, 5, 0, 0, 0], 
    [0, 9, 8, 0, 0, 0, 0, 6, 0], 
    [8, 0, 0, 0, 6, 0, 0, 0, 3], 
    [4, 0, 0, 8, 0, 3, 0, 0, 1], 
    [7, 0, 0, 0, 2, 0, 0, 0, 6], 
    [0, 6, 0, 0, 0, 0, 2, 8, 0], 
    [0, 0, 0, 4, 1, 9, 0, 0, 5], 
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved = solve_sudoku(sudoku_board)
for row in solved:
    print(row)
