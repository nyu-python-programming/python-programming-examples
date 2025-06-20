"""
The game of Tic Tac Toe.
Using lists!
"""


def print_board(row_1, row_2, row_3):
    """
    Print out the game board nicely.
    """
    print("\nThe board:\n")
    print(f"{row_1[0]} | {row_1[1]} | {row_1[2]}")
    print(f"----------")
    print(f"{row_2[0]} | {row_2[1]} | {row_2[2]}")
    print(f"----------")
    print(f"{row_3[0]} | {row_3[1]} | {row_3[2]}")


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
        move = input(f"{player}'s turn: where would you like to go? (row,col) ")
        move = move.split(",")  # get a list of the two numbers as strings
        row = int(move[0])
        col = int(move[1]) - 1  # list indexes start from zero, not 1

        # update the board... only if the row/column the user chose is empty
        if row == 1 and row_1[col].strip() == "":
            # the user chose a column in row 1 that is empty... make the move
            row_1[col] = player
        elif row == 2 and row_2[col].strip() == "":
            # the user chose a column in row 2 that is empty... make the move
            row_2[col] = player
        elif row == 3 and row_3[col].strip() == "":
            # the user chose a column in row 3 that is empty... make the move
            row_3[col] = player
        else:
            # the user entered an invalid row or the row/column they picked is not empty
            print("Sorry, that's an invalid move! Try again.")
            continue  # go to the next iteration of the loop without switching players

        # the move has been made...
        # print out the board to see the update
        print_board(row_1, row_2, row_3)

        # check for a win...
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

        # end the game if there's a winner!
        if win:
            print(f"\n{player} wins!!!\n")
            game_over = True  # change the flag value!  This will stop the loop at the start of the next iteration

        # alternate turns
        if player == "X":
            player = "O"
        else:
            player = "X"


# if running this file directly, call the main function
if __name__ == "__main__":
    main()
