game_is_finished = False

current_player = "X"

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# ======================================================================================================================
# ======================================================================================================================

def display_board():
    """
    Displays the board
    :return: NONE
    """

    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")  # Prints first layer of the board
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")  # Prints second layer of the board
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")  # Prints third layer of the board
    print("\n")


# ======================================================================================================================
# ======================================================================================================================

def do_turn():
    """
    Performs a typical turn in tic tac toe.
    Gets the user input on where they want to go on the board and depending on whose turn it is and if it's available
    places the appropriate sign there.
    :return: NONE
    """

    print("It's " + current_player + "'s turn!\n\n")  # Prints the players turn

    position = input("Choose a position from 1-9: ")  # Gets user input for wanted position

    print("\n\n")

    try:  # Tries to correct position

        position = int(position) - 1

    except ValueError:  # They did not type in a number

        print("Sorry that is invalid\n\n")

        do_turn()  # Repeats the turn

        return

    try:  # Put an "X" at the position chosen

        if board[position] == "-":  # If it is empty

            board[position] = current_player  # Fills it with, "current_player"

        else:

            print("That spot is taken. Go again.\n\n")

            do_turn()

            return

    except IndexError:  # If their number is not in the boards range

        print("That number is not valid\n\n")

        do_turn()

        return


# ======================================================================================================================
# ======================================================================================================================

def switch_player():
    """
    Changes the player from "X" to "O" or from "O" to "X".
    :return: NONE
    """

    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"


# ======================================================================================================================
# ======================================================================================================================

def check_for_winner():
    """
    Checks the rows, columns and diagonals to see if there is someone, who was won, and if not nothing happens and the
    game continues as normal until the game is won or the game is a tie (see line 172).
    :return: NONE
    """

    global game_is_finished

# ======================================================================================================================
# This section of code checks the rows for a victory

    row_1 = board[0] + board[1] + board[2]
    row_2 = board[3] + board[4] + board[5]
    row_3 = board[6] + board[7] + board[8]

    if row_1 == "XXX" or row_2 == "XXX" or row_3 == "XXX":  # Checks rows to see if "X" has won

        display_board()  # Displays final board

        print("X Won!\n\n")

        game_is_finished = True  # Ends game loop

    elif row_1 == "OOO" or row_2 == "OOO" or row_3 == "OOO":  # Checks rows to see if "O" has won

        display_board()  # Displays final board

        print("O Won!\n\n")

        game_is_finished = True  # Ends game loop

# ======================================================================================================================
# This section of code check the columns for a victory

    column_1 = board[0] + board[3] + board[6]
    column_2 = board[1] + board[4] + board[7]
    column_3 = board[2] + board[5] + board[8]

    if column_1 == "XXX" or column_2 == "XXX" or column_3 == "XXX":  # Checks columns to see if "X" has won

        display_board()  # Displays final board

        print("X Won!\n\n")

        game_is_finished = True  # Ends game loop

    elif column_1 == "OOO" or column_2 == "OOO" or column_3 == "OOO":  # Checks columns to see if "O" has won
        display_board()  # Displays final board

        print("O Won!\n\n")

        game_is_finished = True  # Ends game loop

# ======================================================================================================================
# This section of code checks the diagonals for a victory

    diagonal_1 = board[0] + board[4] + board[8]
    diagonal_2 = board[2] + board[4] + board[6]

    if diagonal_1 == "XXX" or diagonal_2 == "XXX":  # Checks diagonals to see if "X" has won

        display_board()  # Displays final board

        print("X Won!\n\n")

        game_is_finished = True  # Ends game loop

    elif diagonal_1 == "OOO" or diagonal_2 == "OOO":  # Checks diagonals to see if "O" has won

        display_board()  # Displays final board

        print("O Won!\n\n")

        game_is_finished = True  # Ends game loop


# ======================================================================================================================
# ======================================================================================================================

def check_for_tie():
    """
    Checks whether or not there are any empty slots remaining, and if not, the game ends in a tie.
    This check is done after the check to see if someone has won to ensure that last turn wins are accounted for.
    :return: NONE
    """

    global game_is_finished

    if "-" not in board:  # If all of the slots are taken

        display_board()  # Display final board

        print("The game ended in a Tie!\n\n")

        game_is_finished = True  # Ends game loop


# ======================================================================================================================
# ======================================================================================================================

def play_game():
    """
    Plays the entire game in a loop until, "game_is_finished" is True.
    :return:
    """

    while game_is_finished is False:

        display_board()  # Displays the initial board (line 13)

        do_turn()  # Goes through a turn (line 27)

        check_for_winner()  # Checks for a winner (line 97)

        check_for_tie()  # Checks if game has ended in a tie (line 172)

        switch_player()  # Switches the player around (line 79)


# ====================================================Program Starts====================================================
# ======================================================================================================================

play_game()  # Plays the game
