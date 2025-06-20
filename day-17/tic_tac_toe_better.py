"""
The game of Tic Tac Toe, with code organized nicely.
Using lists and single-purpose functions!
"""


def print_board(row_1, row_2, row_3):
    """
    Print out the game board nicely.

    Args:
        row_1 (list): The first row of the Tic Tac Toe board.
        row_2 (list): The second row of the Tic Tac Toe board.
        row_3 (list): The third row of the Tic Tac Toe board.
    """
    print("\nThe board:\n")
    print(f"{row_1[0]} | {row_1[1]} | {row_1[2]}")
    print(f"----------")
    print(f"{row_2[0]} | {row_2[1]} | {row_2[2]}")
    print(f"----------")
    print(f"{row_3[0]} | {row_3[1]} | {row_3[2]}")


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


def is_valid_move(row, col, row_1, row_2, row_3):
    """
    Check if the move is valid.

    Args:
        row (int): The row number (1, 2, or 3).
        col (int): The column index (0, 1, or 2).
        row_1 (list): The first row of the Tic Tac Toe board.
        row_2 (list): The second row of the Tic Tac Toe board.
        row_3 (list): The third row of the Tic Tac Toe board.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    if row == 1 and row_1[col].strip() == "":
        return True
    elif row == 2 and row_2[col].strip() == "":
        return True
    elif row == 3 and row_3[col].strip() == "":
        return True
    return False


def is_win(row_1, row_2, row_3):
    """
    Check if there is a win condition on the board.
    Args:
        row_1 (list): The first row of the Tic Tac Toe board.
        row_2 (list): The second row of the Tic Tac Toe board.
        row_3 (list): The third row of the Tic Tac Toe board.
    Returns:
        bool: True if there is a win, False otherwise.
    """
    win = False
    if row_1[0].strip() != "" and (row_1[0] == row_1[1] == row_1[2]):
        # row 1 win
        win = True
    elif row_2[0].strip() != "" and (row_2[0] == row_2[1] == row_2[2]):
        # row 2 win
        win = True
    elif row_3[0].strip() != "" and (row_3[0] == row_3[1] == row_3[2]):
        # row 3 win
        win = True
    elif row_1[0].strip() != "" and (row_1[0] == row_2[0] == row_3[0]):
        # column 1 win
        win = True
    elif row_1[1].strip() != "" and (row_1[1] == row_2[1] == row_3[1]):
        # column 2 win
        win = True
    elif row_1[2].strip() != "" and (row_1[2] == row_2[2] == row_3[2]):
        # column 3 win
        win = True
    elif row_1[0].strip() != "" and (row_1[0] == row_2[1] == row_3[2]):
        # diagonal win (top left to bottom right)
        win = True
    elif row_1[2].strip() != "" and (row_1[2] == row_2[1] == row_3[0]):
        # diagonal win (top right to bottom left)
        win = True
    return win


def main():
    # initialize the board
    row_1 = [" ", " ", " "]
    row_2 = [" ", " ", " "]
    row_3 = [" ", " ", " "]

    # start with player X
    player = "X"

    # print intitial state of board
    print_board(row_1, row_2, row_3)

    # keep looping until the game is over
    game_over = False
    while not game_over:
        # get the user's desired move
        move = get_user_move(player)  # returns a list [row, col]
        row = move[0]  # get the row from the list
        col = move[1]  # get the column from the list

        # check the move's validity
        if not is_valid_move(row, col, row_1, row_2, row_3):
            # the user entered an invalid row or the row/column they picked is not empty
            print("Sorry, that's an invalid move! Try again.")
            continue  # go to the next iteration of the loop without switching players

        # it's valid... update the board
        if row == 1:
            # the user chose a column in row 1 that is empty... make the move
            row_1[col] = player
        elif row == 2:
            # the user chose a column in row 2 that is empty... make the move
            row_2[col] = player
        elif row == 3:
            # the user chose a column in row 3 that is empty... make the move
            row_3[col] = player

        # the move has been made...
        # print out the board to see the update
        print_board(row_1, row_2, row_3)

        # check for a win...
        win = is_win(row_1, row_2, row_3)

        # end the game if there's a winner!
        if win:
            print(f"\n{player} wins!!!\n")
            game_over = True  # change the flag value!  This will stop the loop at the start of the next iteration

        # alternate turns
        player = get_next_player(player)  # get the next player


# if running this file directly, call the main function
if __name__ == "__main__":
    main()
