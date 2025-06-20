"""
The game of Tic Tac Toe, with code organized nicely.
Using a two-dimensional list and single-purpose functions!
"""


def print_board(board):
    """
    Print out the game board nicely.

    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
    """
    print("\nThe board:\n")
    # loop through each inner list (row) and print it out
    for row in board:
        print(f"{row[0]} | {row[1]} | {row[2]}")
        print(f"----------")


def get_next_player(current_player):
    """
    Determine who the next player is.

    Args:
        current_player (str): The current player, either "X" or "O".

    Returns:
        str: The next player whose turn it is, either "X" or "O".
    """
    # alternate turns
    if current_player == "X":
        next_player = "O"
    else:
        next_player = "X"
    return next_player


def get_user_move(current_player):
    """
    Prompts the current player to enter their move as a row and column.

    Args:
        current_player (str): The symbol representing the current player, either "X" or "O".

    Returns:
        list: A list containing two integers [row, col], where 'row' is the row number (as entered)
              and 'col' is the zero-based column index for the move.

    Example:
        If the user inputs "2,3", the function returns [2, 2].
    """
    move = input(f"{current_player}'s turn: where would you like to go? (row,col) ")
    move = move.split(",")  # get a list of the two numbers as strings
    row = int(move[0])
    col = int(move[1]) - 1  # list indexes start from zero, not 1
    move = [row, col]
    return move


def is_valid_move(row, col, board):
    """
    Check if the move is valid.

    Args:
        row (int): The row number (1, 2, or 3).
        col (int): The column index (0, 1, or 2).
        board (list): A 2D list representing the Tic Tac Toe board.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    if board[row - 1][col].strip() == "":
        return True
    return False


def is_win(board):
    """
    Check if there is a win condition on the board.
    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
    Returns:
        bool: True if there is a win, False otherwise.
    """
    win = False
    # Check rows for win
    for row in range(3):
        # Check if the row is not empty and all elements are the same
        if (
            board[row][0].strip() != ""
            and board[row][0] == board[row][1] == board[row][2]
        ):
            win = True
            return win

    # Check columns for win
    for col in range(3):
        # Check if the column is not empty and all elements are the same
        if (
            board[0][col].strip() != ""
            and board[0][col] == board[1][col] == board[2][col]
        ):
            win = True
            return win

    # Check diagonals for win
    if board[0][0].strip() != "" and board[0][0] == board[1][1] == board[2][2]:
        win = True
    elif board[0][2].strip() != "" and board[0][2] == board[1][1] == board[2][0]:
        win = True

    return win


def make_move(board, row, col, player):
    """
    Make a move on the board.

    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
        row (int): The row number (1, 2, or 3).
        col (int): The column index (0, 1, or 2).
        player (str): The symbol of the player making the move ("X" or "O").

    Returns:
        list: The updated board after the move has been made.
    """
    board[row - 1][col] = player
    return board


def main():
    # initialize the board as a 2D list
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

    # start with player X
    player = "X"

    # print intitial state of board
    print_board(board)

    # keep looping until the game is over
    game_over = False
    while not game_over:
        # get the user's desired move
        move = get_user_move(player)  # returns a list [row, col]
        row = move[0]  # get the row from the list
        col = move[1]  # get the column from the list

        # check the move's validity
        if not is_valid_move(row, col, board):
            # the user entered an invalid row or the row/column they picked is not empty
            print("Sorry, that's an invalid move! Try again.")
            continue  # go to the next iteration of the loop without switching players

        # it's valid... update the board
        board = make_move(board, row, col, player)

        # the move has been made...
        # print out the board to see the update
        print_board(board)

        # check for a win...
        win = is_win(board)

        # end the game if there's a winner!
        if win:
            print(f"\n{player} wins!!!\n")
            game_over = True  # change the flag value!  This will stop the loop at the start of the next iteration

        # alternate turns
        player = get_next_player(player)  # get the next player


# if running this file directly, call the main function
if __name__ == "__main__":
    main()
