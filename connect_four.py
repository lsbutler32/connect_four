board = [["-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-"]]
winner = False
player_turn = "R"
reverse_board = board[::-1]


def play_chip(choice):
    """
    Plays chips in specified column by user
    :param choice: An input from the user for which column they want
    :return: Checks if the row is taken already and goes to next row to place chip
    """
    for row in reverse_board:
        if row[choice] == '-':
            row[choice] = player_turn
            switch_turn()
            return True
    if reverse_board[-1][choice] != '-':
        print('That column is full. Pick another spot!')
        print(f"It is still {player_turn}'s turn!")


def display_board():
    """
    Print the board
    :return: Updated board with all positions that have been taken
    """
    for i in board:
        print(i)


def play_game():
    """
    Starts the game
    :return: Plays the game until either a winner or tie is found
    """
    display_board()
    print(f"Time to play some connect 4. {player_turn} will go first")
    while winner is False:
        handle_turn()
        find_winner()


def handle_turn():
    """
    Ask player's choice and puts chip in place
    :return: Board with the correct player's chip in inputted slot
    """
    choice = input("Pick a column you would like to place your piece (1-7): ")
    while choice not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Not valid")
        choice = input("Pick a column you would like to place your piece (1-7): ")
    choice = int(choice)
    play_chip(choice - 1)
    display_board()


def switch_turn():
    """
    Switches the player turn
    :return: The next player's turn that needs to go
    """
    global player_turn
    if player_turn == "R":
        player_turn = "B"
    elif player_turn == "B":
        player_turn = "R"
    if winner is False:
        print(f"It is now {player_turn}'s turn")


def find_winner():
    """
    Check for all possible winners, checking horizontal, vertical, and diagonal
    :return: winner is either True or False, if winner is True game ends. If no winners and board is full returns a tie
    """
    global winner
    for i in reverse_board:  # Checking for horizontal winners
        for j in range(4):
            if i[j] == i[j + 1] == i[j + 2] == i[j + 3] and i[j] != '-':
                winner = True
                print(f"Game over {player_turn} has won!")
                return winner
    for i in range(3):  # Check for vertical winners
        for j in range(6):
            if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] and board[i][j] != '-':
                winner = True
                print(f"Game over {player_turn} has won!")
                return winner
    for i in range(3):  # Check diagonal winners
        for j in range(4):
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] and board[i][j] != '-':
                winner = True
                print(f"Game over {player_turn} has won!")
                return winner
    for i in range(3, 6):  # Check diagonal winners
        for j in range(4):
            if board[i][j] == board[i - 1][j + 1] == board[i - 2][j + 2] == board[i - 3][j + 3] and board[i][j] != '-':
                winner = True
                print(f"Game over {player_turn} has won!")
                return winner
    for i in range(6):  # Check for tie
        if '-' not in board[i] and winner is False:
            print('The game is a tie!')


play_game()
