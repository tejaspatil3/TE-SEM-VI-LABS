class NQueensBacktracking:
    def __init__(self, N):
        self.N = N  # Size of the board (NxN)
        self.board = [-1] * N  # Board to store the column positions of queens

    # Function to check if a queen can be placed at board[row]
    def is_safe(self, row, col):
        for i in range(row):
            # Check if the column or diagonals are under attack
            if self.board[i] == col or abs(self.board[i] - col) == abs(i - row):
                return False
        return True

    # Function to solve the N-Queens problem using backtracking
    def solve(self, row):
        if row == self.N:
            self.print_solution()
            return True

        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row] = col
                if self.solve(row + 1):  # Try to place queens in the next row
                    return True
                self.board[row] = -1  # Backtrack if no valid position found

        return False

    # Function to print the solution
    def print_solution(self):
        for i in range(self.N):
            row = ['Q' if self.board[i] == j else '.' for j in range(self.N)]
            print(" ".join(row))
        print("\n")


# Test the Backtracking approach
N = 8
n_queens = NQueensBacktracking(N)
if not n_queens.solve(0):
    print("Solution does not exist")



# Backtracking – O(n*n!) Time and O(n*n) Space