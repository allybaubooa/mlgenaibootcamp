# Tic Tac Toe game

def create_board():
    # Create and return an empty 3x3 board.
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    print("\n   1   2   3")
    for i, row in enumerate(board, start=1):
        print(f"{i}  " + " | ".join(row))
        if i < 3:
            print("  ---+---+---")
    print()  


def player_input(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): "))
            col = int(input(f"Player {player}, enter column (1-3): "))

            # Convert to 0-based index
            row -= 1
            col -= 1

            # Check valid range
            if row not in range(3) or col not in range(3):
                print("Invalid position. Please choose numbers between 1 and 3.")
                continue

            # Check if cell is empty
            if board[row][col] != " ":
                print("Cell is already taken. Try again.")
                continue

            return row, col

        except ValueError:
            print("Please enter valid numbers (1–3).")


def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_tie(board):
    for row in board:
        if " " in row:
            return False
    return True


def switch_player(player):
    #Return the other player's symbol.
    return "O" if player == "X" else "X"


def play():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)

        # Get move
        row, col = player_input(board, current_player)
        board[row][col] = current_player

        # Check for win
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for tie
        if is_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = switch_player(current_player)


# Run the game
if __name__ == "__main__":
    play()
