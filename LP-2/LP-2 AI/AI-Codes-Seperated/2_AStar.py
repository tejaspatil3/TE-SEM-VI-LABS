import copy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (4 * len(board) - 1))

def check_winner(board, player):
    n = len(board)

    # Check rows and columns
    for i in range(n):
        if all(board[i][j] == player for j in range(n)) or \
           all(board[j][i] == player for j in range(n)):
            return True

    # Check main diagonal
    if all(board[i][i] == player for i in range(n)):
        return True

    # Check anti-diagonal
    if all(board[i][n - 1 - i] == player for i in range(n)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == " "]

def heuristic(board, player):
    if check_winner(board, 'O'):
        return -10
    elif check_winner(board, 'X'):
        return 10
    return 0

def best_move(board):
    best_score = -float('inf')
    move = None
    for (i, j) in get_empty_cells(board):
        temp_board = copy.deepcopy(board)
        temp_board[i][j] = 'X'
        score = search(temp_board, False)
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def search(board, is_max):
    if check_winner(board, 'X') or check_winner(board, 'O') or is_full(board):
        return heuristic(board, 'X')

    if is_max:
        best = -float('inf')
        for (i, j) in get_empty_cells(board):
            board[i][j] = 'X'
            best = max(best, search(copy.deepcopy(board), False))
            board[i][j] = " "
        return best
    else:
        best = float('inf')
        for (i, j) in get_empty_cells(board):
            board[i][j] = 'O'
            best = min(best, search(copy.deepcopy(board), True))
            board[i][j] = " "
        return best

def play():
    size = int(input("Enter board size (3 or more): "))
    board = [[" "]*size for _ in range(size)]  # it will create a 2-D matrix [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    print(f"You are O, Computer is X — Board size: {size}x{size}")
    print_board(board)

    while True:
        try:
            row, col = map(int, input(f"Enter your move (row col 0-{size-1}): ").split())
        except:
            print("Invalid input. Please enter row and col separated by space.")
            continue

        if not (0 <= row < size and 0 <= col < size) or board[row][col] != " ":
            print("Invalid move, try again.")
            continue

        board[row][col] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'X'
            print("Computer's move:")
            print_board(board)
            if check_winner(board, 'X'):
                print("Computer wins!")
                break
        else:
            print("It's a draw!")
            break

        if is_full(board):
            print("It's a draw!")
            break

play()