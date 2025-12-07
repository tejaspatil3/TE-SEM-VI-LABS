class NQueensBranchAndBound:
    def __init__(self, N):
        self.N = N  # Size of the board (NxN)
        self.board = [-1] * N  # Board to store the column positions of queens
        self.blocked_columns = set()  # Set to store blocked columns
        self.blocked_left_diagonals = set()  # Set for left diagonals
        self.blocked_right_diagonals = set()  # Set for right diagonals

    # Function to check if a queen can be placed at board[row]
    def is_safe(self, row, col):
        if col in self.blocked_columns or (row - col) in self.blocked_left_diagonals or (row + col) in self.blocked_right_diagonals:
            return False
        return True

    # Function to solve the N-Queens problem using Branch and Bound
    def solve(self, row):
        if row == self.N:
            self.print_solution()
            return True

        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row] = col
                self.blocked_columns.add(col)
                self.blocked_left_diagonals.add(row - col)
                self.blocked_right_diagonals.add(row + col)

                if self.solve(row + 1):  # Try to place queens in the next row
                    return True

                # Backtrack
                self.board[row] = -1
                self.blocked_columns.remove(col)
                self.blocked_left_diagonals.remove(row - col)
                self.blocked_right_diagonals.remove(row + col)

        return False

    # Function to print the solution
    def print_solution(self):
        for i in range(self.N):
            row = ['Q' if self.board[i] == j else '.' for j in range(self.N)]
            print(" ".join(row))
        print("\n")


# Test the Branch and Bound approach
N = 8
n_queens = NQueensBranchAndBound(N)
if not n_queens.solve(0):
    print("Solution does not exist")
