def isSafe(board, row, col, N):
    # Check left side of current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True
# def isSafe(board, row, col, N):
#     # Check left (same row)
#     for i in range(col - 1, -1, -1):
#         if board[row][i] == 1:
#             return False

#     # Check right (same row)
#     for i in range(col + 1, N):
#         if board[row][i] == 1:
#             return False

#     # Check upward (same column)
#     for i in range(row - 1, -1, -1):
#         if board[i][col] == 1:
#             return False

#     # Check downward (same column)
#     for i in range(row + 1, N):
#         if board[i][col] == 1:
#             return False

#     return True


def solveNQUtil(board, col, N):
    # Base case: if all queens are placed
    if col >= N:
        return True

    # Try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1  # Place the queen

            # Recurse to place rest of the queens
            if solveNQUtil(board, col + 1, N):
                return True

            # If placing queen at (i, col) doesn't lead to solution, backtrack
            board[i][col] = 0

    return False

def printSolution(N):
    board = [[0] * N for _ in range(N)]

    if not solveNQUtil(board, 0, N):
        print("Solution does not exist")
        return False

    print("Solution found for", N, "queens:")
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    return True

# Input from user
n = int(input("Number of queens to place: "))
printSolution(n)
