solutions = []  # store all solutions


def take_input():
    while True:
            n = int(input("Input size of chessboard? n = "))
            if n <= 3:
                print("Enter a value >= 4")
            else:
                return n
                
def get_board(n):
    return [["x" for _ in range(n)] for _ in range(n)]


def is_safe(board, row, col, n):
    # same row on left
    for j in range(col):
        if board[row][j] == "Q":
            return False

    # upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # lower diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True


def add_solution(board):
    sol = [row[:] for row in board]
    solutions.append(sol)


def solve(board, col, n):
    if col == n:
        add_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = "Q"
            solve(board, col + 1, n)
            board[i][col] = "x"  # backtrack


def print_solution(n):
    if not solutions:
        print("No solutions found.")
        return
        
    for row in solutions[0]:
        print(" ".join(row))


# MAIN
n = take_input()
board = get_board(n)
solve(board, 0, n)

print("\nOne of the solutions:\n")
print_solution(n)

print(f"\nTotal number of solutions = {len(solutions)}")
