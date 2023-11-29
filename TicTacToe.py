import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def human_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return -1
    elif check_winner(board, "X"):
        return 1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for row, col in get_empty_cells(board):
            board[row][col] = "X"
            eval = minimax(board, depth + 1, False)
            board[row][col] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for row, col in get_empty_cells(board):
            board[row][col] = "O"
            eval = minimax(board, depth + 1, True)
            board[row][col] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for row, col in get_empty_cells(board):
        board[row][col] = "X"
        move_val = minimax(board, 0, False)
        board[row][col] = " "

        if move_val > best_val:
            best_move = (row, col)
            best_val = move_val

    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            row, col = human_move(board)
        else:
            print("AI is making a move...")
            row, col = best_move(board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
