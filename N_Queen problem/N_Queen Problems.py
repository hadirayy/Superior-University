def print_Board(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end= " ")
        print()
    print()
def is_safe(board,row,col,n):
    for i in range(row):
        if board[i][col] == "Q":
            return False
    i,j = row ,col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -=1
        j -=1
    i,j = row ,col
    while i>= 0 and j < n:
        if board [i][j] == "Q":
            return False
        i -= 1
        j += 1
    return True
def solve(board,row,n):
    if row == n:
        print_Board(board,n)
        return True
    for col in range(n):
        if is_safe(board, row ,col,n):
            board[row][col]="Q"
            if solve(board,row +1 ,n):
                return True
            board [row][col] ="."
    return False
def n_queen(n):
    board = [["."] * n for _ in range(n)]
    if not solve(board,0,n):
        print("No solution exists for ",n,"x",n,"board")
n=int(input("Enter the number of Board(rows and colums):"))
n_queen(n)